from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class supplier_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=225)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.supplier_name