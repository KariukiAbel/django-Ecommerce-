from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name = 'signup'),
    path('', views.login_view, name = 'login'),
    path('password_reset/', views.reset_password, name= 'reset_password'),
]