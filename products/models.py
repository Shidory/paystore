from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100,
                                     blank=True, null=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.FileField(upload_to='products/images/', null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title
