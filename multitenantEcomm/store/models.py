#from django_tenants.models import TenantMixin, DomainMixin
import os

from django.db import models
from scripts.logger import get_logger

logger = get_logger('owner_actions.log')

# Tenant model representing a client in the multi-tenant system
#class Tenant(TenantMixin):
#    name = models.CharField(max_length=100)  # Name of the tenant
#    paid_until = models.DateField()  # Date until which the tenant has paid
#    on_trial = models.BooleanField(default=True)  # Whether the tenant is on a trial period
#
#    auto_create_schema = True  # Automatically create a database schema for each tenant
#
## Domain model for associating domains with tenants
#class Domain(DomainMixin):
#    pass  # Using the default implementation from DomainMixin


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    picture = models.ImageField(upload_to='store/images/products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def delete_model(self, request, obj):
        if obj.picture:
            logger.info(f"Deleting image: {obj.picture}")
            image_path = "store/images/products/" + obj.picture.name
            if os.path.exists(image_path):
                os.remove(image_path)
                logger.info(f"The image '{image_path}' was deleted successfully.")
           
        logger.info(f"Deleting product from database: {obj.name}")
        super().delete_model(request, obj)