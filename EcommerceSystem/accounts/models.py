from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    town = models.CharField(max_length = 255)
    date_registered = models.DateField(auto_now_add = True)
    user_type = models.IntegerField(default = 2);