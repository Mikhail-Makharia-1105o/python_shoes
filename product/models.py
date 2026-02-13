from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    stock = models.IntegerField(verbose_name="Количество на складе")
    manufacturer = models.ForeignObject("Manufacturer", related_name="manufacturer", on_delete=models.CASCADE, verbose_name="Производитель")
    supplier = models.ForeignObject("Supplier", related_name="supplier", on_delete=models.CASCADE, verbose_name="Поставщик")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    address = models.TextField(verbose_name="Адрес")
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.SET_NULL, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    def __str__(self):
        return self.product

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart", on_delete=models.SET_NULL, verbose_name="Корзина")
    product = models.ForeignKey(Product, related_name="product", on_delete=models.SET_NULL, verbose_name="Товар")
    quantity = models.IntegerField(verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    def __str__(self):
        return self.product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ['name', 'price', 'description', 'image', 'stock', 'manufacturer', 'supplier']

