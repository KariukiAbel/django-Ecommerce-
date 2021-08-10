from django.shortcuts import render, redirect
from .models import Product


# Create your views here.
def index_view(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})

def product_details_view(request):
    # context = {}
    return render(request, 'products/details.html')
