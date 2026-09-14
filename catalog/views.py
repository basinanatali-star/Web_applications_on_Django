from itertools import product
from django.shortcuts import render
from django.utils.translation.trans_real import catalog
from .models import Product


def home_view(request):
    return render(request, 'home.html')


def contacts_view(request):
    return render(request, 'contacts.html')


def index(request):
    return render(request, 'products_list.html')


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)