from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/pages/home.html', status=200, context=
        {
            'products': products
        }
    )
