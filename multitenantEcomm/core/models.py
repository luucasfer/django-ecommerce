from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User

STATUS_CHOICES = (
    ("processando", "Processando"),
    ("enviado", "Enviado"),
    ("entregue", "Entregue")
)

STATUS = (
    ("desabilitado", "Desabilitado"),
    ("em analise", "Em analise"),
    ("publicado", "Publicado")
)

RATING = (
    (0, "Não avaliado"),
    (1, "⭐☆☆☆☆"),
    (2, "⭐⭐☆☆☆"),
    (3, "⭐⭐⭐☆☆"),
    (4, "⭐⭐⭐⭐☆"),
    (5, "⭐⭐⭐⭐⭐")
)



def product_directory_path(instance, filename):
    return 'products/{0}/{1}'.format(instance.product_id, filename)


def validate_image(value):
    if value.file.size > 5 * 1024 * 1024:
        raise ValidationError("A imagem deve ter menos de 5MB.")
    if value.file.content_type not in ['image/jpeg', 'image/png']:
        raise ValidationError("Formato de imagem inválido. Apenas JPEG e PNG são permitidos.")

    return value   




########################################################
########### Category, Tags and Product ################
########################################################

class Category(models.Model):
    category_id = ShortUUIDField(unique=True, primary_key=True, length=10, max_length=20, prefix="cat", alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/") #, validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def category_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image available"


    def __str__(self):

        return self.title


class Tags(models.Model):
    pass


class Product(models.Model):
    product_id = ShortUUIDField(unique=True, primary_key=True, length=10, max_length=20, prefix="prod", alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category') # if category is deleted, set the product category to NULL
    actual_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    old_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)
    stock_amount = models.IntegerField(validators=[MinValueValidator(0)], default=1)
    in_stock = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    specifications = models.TextField(max_length=1000, null=True, blank=True)
    #tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(max_length=20, choices=STATUS, default="publicado")
    rating = models.IntegerField(choices=RATING, default=0)
    sold_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Produtos'

    def product_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image available"

    def __str__(self):
        return self.title

    def get_percentage_discount(self):
        if self.old_price and self.actual_price:
            return round(((self.old_price - self.actual_price) / self.old_price) * 100)
        return 0


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_directory_path) #, validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Imagens do produto'




########################################################
########### Cart, Order and Order Items ################
########################################################

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="processando")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Pedidos'



class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Itens do carrinho'

    def order_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image}" width="50" height="50" />')
        return "No image available"



########################################################
######### Product Review, Wishlist and Address #########
########################################################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATING, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Avaliações dos produtos'

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Lista de desejos'
    
    def __str__(self):
        return self.product.title

    


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Endereços'

    def __str__(self):

        return self.address


