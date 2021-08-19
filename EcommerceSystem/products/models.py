from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add = True)
    price = models.FloatField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    in_store = models.BooleanField(default="True")
    
    
    def __str__(self):
        return f"{self.name}"
    
    
class Product_description(models.Model):
    image = models.ImageField()
    category = models.CharField(max_length=100)
    unit_description = models.CharField(max_length= 100)
    description = models.TextField(max_length=255)
    quantity = models.IntegerField()
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.description}'
