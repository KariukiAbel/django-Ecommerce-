from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def signup_view(request):
    return render(request, 'accounts/signup.html')

def login_view(request):
    return render(request, 'accounts/login.html')
