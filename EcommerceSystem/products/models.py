from django.db import models
from django.contrib.auth.models import User
from suppliers.models import supplier_details

# Create your models here.        
class Unit(models.Model):
    unit_name = models.CharField(max_length =100)
    
    def __str__(self):
        return self.unit_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
    
class Product_description(models.Model):
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    unit_description = models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null =True)
    description = models.TextField(max_length=255)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(supplier_details, on_delete=models.CASCADE)
        
    
    def __str__(self):
        return self.description

class Product(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add = True)
    price = models.FloatField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    in_store = models.BooleanField(default="True")
    product_description = models.OneToOneField(Product_description, on_delete=models.CASCADE)

    
    
    def __str__(self):
        return self.name