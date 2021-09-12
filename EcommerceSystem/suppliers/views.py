from django.shortcuts import render
from products.models import Product


# Create your views here.
def product_view(request):
    supplier_products = Product.objects.all()
    return render(request, 'suppliers/index.html', {'products': supplier_products})

# def add_product_view(request):
#     return render(request,)