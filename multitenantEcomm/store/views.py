from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', status=200, context=
        {
            'products': products
        }
    )
