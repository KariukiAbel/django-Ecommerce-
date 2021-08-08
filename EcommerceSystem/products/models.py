from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    image = models.ImageField(default='default.png', blank=True)
    date_added = models.DateField(auto_now_add = True)
    price = models.FloatField(max_length=100)
    category = models.CharField(max_length=100)
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.name}-{self.image}"
