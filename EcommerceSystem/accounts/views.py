from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup_view(request):
    return render(request, 'accounts/login.html')

def login_view():
    pass