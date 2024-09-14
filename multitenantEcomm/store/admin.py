from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock', 'picture')
    search_fields = ('name',)
    list_filter = ('name', 'price', 'stock')
    list_editable = ('price', 'stock')
    list_per_page = 10

