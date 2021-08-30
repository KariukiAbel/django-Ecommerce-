from django.urls import path
from products import views

app_name="products"

urlpatterns = [
      path('', views.index_view, name='index'),
      path('details/<pk>', views.product_details_view, name='details'),
      path('search/' , views.search_view, name='search'),
]
