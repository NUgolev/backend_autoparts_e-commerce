# Generated by Django 2.2.26 on 2022-01-28 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_auto_20220128_1915"),
    ]

    operations = [
        migrations.CreateModel(
            name="Filter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(verbose_name="Название фильтра")),
            ],
            options={
                "db_table": "filter",
                "permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_name", models.TextField(verbose_name="Имя клиента")),
                ("client_surname", models.TextField(verbose_name="Фамилия клиента")),
                ("phone", models.TextField(verbose_name="Телефон")),
                ("address", models.TextField(verbose_name="Адрес")),
            ],
            options={
                "db_table": "order",
                "permissions": (),
            },
        ),
        migrations.CreateModel(
            name="PayType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(verbose_name="Название способа оплаты")),
            ],
            options={
                "db_table": "pay_type",
                "permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(verbose_name="Название товара")),
                ("price", models.FloatField(verbose_name="Цена")),
                ("image_path", models.TextField(verbose_name="Путь до файла")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
            options={
                "db_table": "product",
                "permissions": (),
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="childs",
                to="api.Category",
                verbose_name="Родительская категория",
            ),
        ),
        migrations.CreateModel(
            name="ProductFilterValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.TextField(verbose_name="Значение")),
                (
                    "filter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Filter",
                        verbose_name="Фильтр",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "db_table": "product_filter_value",
                "permissions": (),
            },
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="products",
                to="api.Category",
                verbose_name="Категория",
            ),
        ),
        migrations.CreateModel(
            name="OrderProducts",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(verbose_name="Количество")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Order",
                        verbose_name="Заказ",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="api.Product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "db_table": "order_products",
                "permissions": (),
            },
        ),
        migrations.AddField(
            model_name="order",
            name="pay_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orders",
                to="api.PayType",
                verbose_name="Способ оплаты",
            ),
        ),
        migrations.AddField(
            model_name="filter",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="filters",
                to="api.Category",
                verbose_name="Категория",
            ),
        ),
    ]