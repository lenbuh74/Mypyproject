from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order, CustomerOrder
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail



@staff_member_required
def AdminOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

def OrderCreate(request):
    cart = Cart(request)


    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.cupon:
                order.cupon = cart.cupon
                order.discount = cart.cupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                User = get_user_model()
                user_email = [a.email for a in User.objects.all()]
                for email in user_email:
                    if email == order.email:
                        CustomerOrder.objects.create(order=order, product=item['product'],email=email
                                                    )
            cart.clear()



            request.session['order_id'] = order.id
            subject = 'Магазин украшений Липской Ирины - заказ {}'.format(order.id)
            message = '{}, вы успешно сделали заказ.\
                                       Номер Вашего заказа {}'.format(order.first_name, order.id)
            send_mail(subject, message, "lenbuh74@mail.ru", [order.email])
            return redirect(reverse('payment:process'))



    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})



def CustomerOrders(request):

    if request.user.is_authenticated:
        orderid_list=[]
        print (request.user.username, request.user.email)
        email = request.user.email
        order_list = [order.order_id for order in CustomerOrder.objects.all().filter(email=email)]
        for id in order_list:
            if id not in orderid_list:
                orderid_list.append(id)
    return render(request, 'customer/customer.html', {'orderid_list': orderid_list})


def CustomerOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'customer/detail.html', {'order': order})






