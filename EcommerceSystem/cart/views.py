from django.shortcuts import render

# Create your views here.

def cart_view(request):
    return render(request, 'cart/index.html')

def checkout_view(request):
    context = {}
    return render(request, 'cart/checkout.html', context)