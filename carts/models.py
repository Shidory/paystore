from django.db import models
from products.models import Product

class Cart:
    products = models.ManyToManyField(Product)
