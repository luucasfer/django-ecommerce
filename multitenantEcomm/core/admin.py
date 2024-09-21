import os
import shutil

from core.models import (Address, CartOrder, CartOrderItem, Category, Product,
                         ProductImages, ProductReview, Tags, Wishlist)
from django.contrib import admin
from django.db.models.signals import post_delete
from django.dispatch import receiver


class ProductImagesAdmin(admin.TabularInline): 
    model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ('product_id', 'title', 'description', 'category', 'actual_price', 'old_price', 'stock_amount', 'in_stock', 'status', 'specifications', 'product_status', 'rating', 'created_at') #, 'display_product_images')
    list_display_links = ('product_id', 'title')

    #def display_product_images(self, obj):
    #    images = obj.images.all()
    #    if images:
    #        return mark_safe(''.join([f'<img src="{image.image.url}" width="50" height="50" />' for image in images]))
    #    return "No images available"
    #display_product_images.short_description = 'Product Images'

    @receiver(post_delete, sender=ProductImages)
    def delete_product_and_images(sender, instance, **kwargs):
        # if the product was deleted, delete the folder with the images
        if os.path.isdir(f'media/products/{instance.product_id}/'):
            shutil.rmtree(f'media/products/{instance.product_id}/')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'title', 'category_image', 'created_at')
    list_display_links = ('category_id', 'title')

    @receiver(post_delete, sender=Category)
    def delete_category_and_images(sender, instance, **kwargs):
        # if the category was deleted, delete the folder with the images
        if os.path.isdir(f'media/categories/{instance.category_id}/'):
            shutil.rmtree(f'media/categories/{instance.category_id}/')



@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_price', 'paid_status', 'order_date', 'due_date', 'order_status', 'created_at')
    list_display_links = ('user', 'order_price')


@admin.register(CartOrderItem)
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'invoice_number', 'product', 'product_status', 'item', 'image', 'quantity', 'price', 'total', 'created_at')
    list_display_links = ('order', 'invoice_number')


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'review', 'created_at')
    list_display_links = ('user', 'product')


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_display_links = ('user', 'product')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'address', 'status')
    list_display_links = ('user', 'full_name')

