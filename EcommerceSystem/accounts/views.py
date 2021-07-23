from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup_view(request):
    return HttpResponse(request, 'signup.html')

def login():
    