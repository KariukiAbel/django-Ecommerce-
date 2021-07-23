from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField()
    description = models.CharField()
    image = models.CharField()
    date_added = models.DateField()
    price = models.CharField()
    category = models.CharField()
    added_by = models.ForeignKey()
