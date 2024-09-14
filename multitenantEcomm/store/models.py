from django.db import models
from functions.logger import get_logger

logger = get_logger('logs.log')


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    picture = models.ImageField(upload_to=lambda instance, filename: f'store/images/products/{instance.name}/{filename}', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)