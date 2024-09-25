from core.models import (Address, CartOrder, CartOrderItem, Category, Product,
                         ProductImages, ProductReview, Wishlist)
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    products = Product.objects.filter(product_status='publicado').order_by('-rating')

    context = {
        'products': products,

    }
    return render(request, 'core/index.html', status=200, context=context)


def product_list_view(request):
    products = Product.objects.filter(product_status='publicado').order_by('-rating')
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'core/product-list.html', status=200, context=context)


def category_list_view(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'core/category-list.html', status=200, context=context)


def category_product_list_view(request, category_id):
    categories = Category.objects.get(category_id=category_id)
    products = Product.objects.filter(product_status='publicado', category=categories)

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'core/category-product-list.html', status=200, context=context)
