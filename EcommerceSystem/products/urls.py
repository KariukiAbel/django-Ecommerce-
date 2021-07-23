from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
      path(r'index/', views.index_view, name='index'),
]
