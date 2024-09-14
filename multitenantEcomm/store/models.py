#from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

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
    picture = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name