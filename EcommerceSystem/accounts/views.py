from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        return render(request,"products/products.html")
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == "POST":
        return render(request, "products/products.html")
    return render(request, 'accounts/login.html')
