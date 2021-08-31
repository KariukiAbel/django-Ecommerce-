from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def cart_view(request):
    return render(request, 'cart/index.html')

def checkout_view(request):
    context = {}
    return render(request, 'cart/checkout.html', context)


def updateItem(request):
    return JsonResponse('Item was added', safe=False)