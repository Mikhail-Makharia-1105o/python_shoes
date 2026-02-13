from django.db import models
from django.contrib.auth.models import User

# Create your models here.

order_status_choices = {
    "Завершен": "COMPLETED",
    "Новый": "NEW",
}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    article = models.CharField(max_length=100, verbose_name="Артикул")
    price = models.PositiveIntegerField(verbose_name="Цена")
    unit = models.CharField(max_length=10, verbose_name="Единица измерения")
    category = models.CharField(max_length=100, verbose_name="Категория")
    current_sale = models.PositiveIntegerField(verbose_name="Текущая скидка")
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
    
class Order(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.SET_NULL, verbose_name="Пользователь")
    order_number = models.PositiveSmallIntegerField(verbose_name="Номер заказа")
    article = models.CharField(max_length=100, verbose_name="Артикул")
    order_date = models.DateTimeField(verbose_name="Время Заказа")
    deliver_date = models.DateTimeField(verbose_name="Время доставки")
    delivery_address = models.CharField(max_length=100, verbose_name="Адрес доставки")
    delivery_code = models.PositiveIntegerField(verbose_name="Код доставки")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    delivery_status = models.CharField(max_length=100, verbose_name="Статус заказа", choices=order_status_choices)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    def __str__(self):
        return self.product

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name="order", on_delete=models.SET_NULL, verbose_name="Корзина")
#     product = models.ForeignKey(Product, related_name="product", on_delete=models.SET_NULL, verbose_name="Товар")
#     quantity = models.IntegerField(verbose_name="Количество")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
#     def __str__(self):
#         return self.product