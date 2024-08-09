from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    