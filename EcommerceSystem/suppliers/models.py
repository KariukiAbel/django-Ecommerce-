from django.db import models

# Create your models here.
class supplier_details(models.Model):
    supplier_name = models.CharField(max_length=225)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    
    
    def __str__(self):
        return f"{self.supplier_name}"