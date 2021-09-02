from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def cart_view(request):
    return render(request, 'cart/index.html')

def checkout_view(request):
    context = {}
    return render(request, 'cart/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId', productId)
    print('Action', action)
    return JsonResponse('Item was added', safe=False)