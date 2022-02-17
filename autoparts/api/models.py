from django.db import models
from django.db.models import PROTECT, CASCADE

# Create your models here.


class Category(models.Model):
    name = models.TextField(verbose_name="Имя категории")
    parent = models.ForeignKey(
        "self",
        null=True,
        on_delete=CASCADE,
        verbose_name="Родительская категория",
        related_name="children",
    )

    class Meta:
        db_table = "category"
        permissions = ()


class Product(models.Model):
    name = models.TextField(verbose_name="Название товара")
    price = models.FloatField(verbose_name="Цена")
    category = models.ForeignKey(
        Category, on_delete=PROTECT, verbose_name="Категория", related_name="products"
    )
    image_path = models.TextField(verbose_name="Путь до файла")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        db_table = "product"
        permissions = ()


class Filter(models.Model):
    name = models.TextField(verbose_name="Название фильтра")
    category = models.ForeignKey(
        Category, on_delete=PROTECT, verbose_name="Категория", related_name="filters"
    )

    class Meta:
        db_table = "filter"
        permissions = ()


class PayType(models.Model):
    name = models.TextField(verbose_name="Название способа оплаты")

    class Meta:
        db_table = "pay_type"
        permissions = ()


class Order(models.Model):
    client_name = models.TextField(verbose_name="Имя клиента")
    client_surname = models.TextField(verbose_name="Фамилия клиента")
    phone = models.TextField(verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")
    pay_type = models.ForeignKey(
        PayType, on_delete=PROTECT, verbose_name="Способ оплаты", related_name="orders"
    )

    class Meta:
        db_table = "order"
        permissions = ()


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=PROTECT, verbose_name="Продукт")
    count = models.IntegerField(verbose_name="Количество")

    class Meta:
        db_table = "order_products"
        permissions = ()


class ProductFilterValue(models.Model):
    product = models.ForeignKey(
        Product, on_delete=CASCADE, related_name="filter_values", verbose_name="Продукт"
    )
    filter = models.ForeignKey(Filter, on_delete=CASCADE, verbose_name="Фильтр", related_name="values")
    value = models.TextField(verbose_name="Значение")

    class Meta:
        db_table = "product_filter_value"
        permissions = ()
