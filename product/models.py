from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    categories = models.CharField(max_length=256)
    brands = models.CharField(max_length=256)
    warranty = models.CharField(max_length=256)
    sellers = models.CharField(max_length=256)