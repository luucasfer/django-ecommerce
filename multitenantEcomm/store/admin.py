import os

from django.contrib import admin
from django.db.models.signals import post_delete
from django.dispatch import receiver
from functions.logger import get_logger

from .models import Product

logger = get_logger("logs.log")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('name', 'price', 'stock')
    list_editable = ('price', 'stock', 'description', 'name')
    list_per_page = 50

    @receiver(post_delete, sender=Product)
    def delete_product_image(sender, instance, **kwargs):
        if instance.picture:
            if os.path.isfile(instance.picture.path):
                os.remove(instance.picture.path)
                logger.info(f"The image '{instance.picture.name}' was deleted successfully.")
            if os.listdir(f'store/images/products/{instance.name}/') == []:
                os.rmdir(f'store/images/products/{instance.name}/')
                logger.info(f"The folder '{instance.name}' was empty and deleted successfully.")
