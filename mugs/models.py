from django.db import models
from datetime import datetime


class Mug(models.Model):

    class Meta:
        verbose_name_plural = 'Mugs'

    sku = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name