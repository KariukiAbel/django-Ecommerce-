from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
      path(r'', views.index_view, name='index'),
]
