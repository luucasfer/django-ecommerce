import os

from django.contrib import admin
from scripts.logger import get_logger

from .models import Product

logger = get_logger('admin_actions.log')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock', 'picture')
    search_fields = ('name',)
    list_filter = ('name', 'price', 'stock')
    list_editable = ('price', 'stock', 'description', 'name', 'picture')
    list_per_page = 50

    def delete_model(self, request, obj):
        if obj.picture:
            logger.info(f"Deleting image: {obj.picture}")
            image_path = "store/images/products/" + obj.picture.name
            if os.path.exists(image_path):
                os.remove(image_path)
                logger.info(f"The image '{image_path}' was deleted successfully.")
           
        logger.info(f"Deleting product from database: {obj.name}")
        super().delete_model(request, obj)