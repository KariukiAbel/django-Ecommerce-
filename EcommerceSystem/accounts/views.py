from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        return render(request,"products/products.html")
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == "POST":
        user_mail = request.POST.get('uname')
        password_entered = request.POST.get('password')
        print(user_mail)
        print(password_entered)
        return render(request, "products/products.html")
    return render(request, 'accounts/login.html')

def reset_password(request):
    users = Users.objects.all();
    return render(request, 'accounts/resetpassword.html')
