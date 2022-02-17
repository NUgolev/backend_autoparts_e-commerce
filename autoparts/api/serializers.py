from rest_framework import serializers
from .models import Product, Category, Filter, ProductFilterValue


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        return []

    class Meta:
        model = Category
        fields = ["id", "name", "children"]


class RootCategorySerializer(serializers.ModelSerializer):
    children = CategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "children"]


class ProductFilterValueSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    value = serializers.CharField()

    def get_name(self, obj):
        return obj.filter.name

    class Meta:
        model = ProductFilterValue
        fields = ["name", "value"]


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    category = serializers.SlugRelatedField("name", queryset=Category.objects.all())
    category_id = serializers.CharField()
    image_path = serializers.CharField()
    description = serializers.CharField()
    filter_values = ProductFilterValueSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "category",
            "category_id",
            "image_path",
            "description",
            "filter_values",
        ]


class ProductFilterSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    values = serializers.SlugRelatedField("value", many=True, queryset=ProductFilterValue.objects.all())

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "values"
        ]
