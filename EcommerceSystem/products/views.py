from django.shortcuts import render
from .models import *


# Create your views here.
def index_view(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products':products})

def product_details_view(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'products/details.html', {'product': product})

def search_view(request, item):
    product_item = Product.objects.filter(name=item)
    return render(request,'products/search.html',{'product_item':product_item})
    
