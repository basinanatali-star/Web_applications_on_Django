from django.shortcuts import render
from .models import Product, Category


def home_view(request):
    return render(request, 'home.html')


def contacts_view(request):
    return render(request, 'contacts.html')


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def category_page(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_page.html', context)
