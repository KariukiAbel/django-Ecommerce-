from django.urls import path
from products import views

app_name="products"

urlpatterns = [
      path('', views.index_view, name='index'),
      path('details/<str:pk>', views.product_details_view, name='details')
]
