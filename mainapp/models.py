from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Продукт')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    description = models.TextField(null=True)
    image = models.ImageField()

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1) # why default is 1 ?
    total_price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct', blank=True)
    total_products = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.id


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.first_name


class Specification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
