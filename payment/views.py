from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def PaymentProcess(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Заказ {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'RUB',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled'))
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html',{'order':order, 'form':form})


@csrf_exempt
def PaymentDone(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order.paid = True
    order.save()

    subject = 'Магазин украшений Липской Ирины - заказ: {}'.format(order.id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    text_content = strip_tags(html)

    msg = EmailMultiAlternatives(subject, text_content, 'lenbuh74@mail.ru', [order.email])
    msg.attach_alternative(html, "text/html")
    msg.send()
    return render(request, 'payment/done.html')


@csrf_exempt
def PaymentCanceled(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    subject = 'Магазин украшений Липской Ирины - заказ: {}'.format(order.id)
    message = '{}, при оплате заказа {} произошла ошибка. Пожалуйста, повторите оплату.'.format(order.first_name, order.id)
    send_mail(subject, message, "lenbuh74@mail.ru", [order.email])

    return render(request, 'payment/canceled.html')
