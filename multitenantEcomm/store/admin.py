import os

from django.contrib import admin
from django.db.models.signals import post_delete
from django.dispatch import receiver
from functions.logger import get_logger

from .models import Picture, Product

logger = get_logger("logs.log")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('name', 'price', 'stock')
    list_editable = ('price', 'stock', 'description', 'name')
    list_per_page = 50

    @receiver(post_delete, sender=Product)
    def delete_product_and_images(sender, instance, **kwargs):
        # if the product has images, delete them all
        if instance.images:
            for image in instance.images.all():
                if os.path.isfile(image.image.path):
                    os.remove(image.image.path)
                    logger.info(f"The product '{instance.name}' and all its images were deleted successfully.")
                    

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'image')
    search_fields = ('product_id',)
    list_filter = ('product_id',)
    list_per_page = 50

    @receiver(post_delete, sender=Picture)
    def delete_images_from_product(sender, instance, **kwargs):
        if instance.image:
            #remove the image from the folder
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
                logger.info(f"The image '{instance.image}' was deleted successfully.")
            # remove the folder if it is empty
            if os.listdir(f'media/products/{instance.product.name}/') == []:
                os.rmdir(f'media/products/{instance.product.name}/')
                logger.info(f"The folder '{instance.product.name}' was empty and deleted successfully.")
