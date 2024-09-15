from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from functions.logger import get_logger

logger = get_logger('logs.log')

def validate_image(value):
    if value.file.size > 10 * 1024 * 1024:
        raise ValidationError("Picture size must be less than 10MB.")
    if value.file.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
        raise ValidationError("Invalid image format. Only JPEG, PNG, and JPG are allowed.")
    return value    


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Picture(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/images/products/', null=True, blank=True) #, validators=[validate_image])

    def __str__(self):
        return f"Image for {self.product.name}"

    def save(self, *args, **kwargs):
        # create a folder for each product to agregate the images
        self.image.field.upload_to = f'store/images/products/{self.product.name}/'
        super().save(*args, **kwargs)