from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Category, Product
from .forms import CommentForm



def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    comments = product.comments.filter(active=True)

    if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.product = product
                new_comment.save()
    else:
            comment_form = CommentForm()

    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'comments': comments,
                           'comment_form': comment_form})


