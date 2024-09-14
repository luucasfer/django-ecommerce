from rest_framework import serializers
from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock must be greater than zero.")
        return value
    def validate_name(self, value):
        if value.isalpha():
            raise serializers.ValidationError("Name cannot be all numbers.")
        return value
    def validate_picture(self, value):
        if value.size > 10 * 1024 * 1024:
            raise serializers.ValidationError("Picture size must be less than 10MB.")
        if value.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
            raise serializers.ValidationError("Invalid image format.")
        return value    
    
