from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import *

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
    
    customer = request.user
    product = Product_description.objects.get(id=productId)
    return JsonResponse('Item was added', safe=False)