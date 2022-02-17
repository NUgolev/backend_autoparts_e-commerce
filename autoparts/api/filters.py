import django_filters
from django.db.models import Case, F, When, Value, CharField, Q
from django.db.models.functions import Concat
from api.models import Product, Category, Filter


class CategoryFilter(django_filters.FilterSet):
    root = django_filters.BooleanFilter(field_name="parent", lookup_expr="isnull")

    class Meta:
        model = Category
        fields = ["root"]


def get_category_choices():
    choices = tuple((c.name, c.name) for c in Category.objects.all())
    return choices


class ProductFilter(django_filters.FilterSet):
    price_gte = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    category = django_filters.NumberFilter(
        method="category_filter", label="Поиск id категории"
    )
    ordering = django_filters.OrderingFilter(
        fields=(
            ("price", "price"),
            ("id", "id"),
        )
    )
    search = django_filters.CharFilter(
        method="search_filter", label="Поиск по названию/описанию"
    )

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )

    def category_filter(self, queryset, name, value):
        where = f"category_id = any(get_children({value}))"
        return queryset.extra(where=[where])

    class Meta:
        model = Product
        fields = ["price_gte", "price_lte", "category", "ordering"]


class ProductFilterFilter(django_filters.FilterSet):
    price_gte = django_filters.NumberFilter(field_name="values__product__price", lookup_expr="gte")
    price_lte = django_filters.NumberFilter(field_name="values__product__price", lookup_expr="lte")
    ordering = django_filters.OrderingFilter(
        fields=(
            ("price", "values__product__price"),
            ("id", "values__product__id"),
        )
    )
    category = django_filters.NumberFilter(
        method="category_filter", label="Поиск id категории"
    )
    search = django_filters.CharFilter(
        method="search_filter", label="Поиск по названию/описанию"
    )

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(values__product__name__icontains=value) | Q(values__product__description__icontains=value)
        )

    def category_filter(self, queryset, name, value):
        where = f"category_id = any(get_children({value}))"
        return queryset.extra(where=[where])

    class Meta:
        model = Filter
        fields = ["price_gte", "price_lte", "category", "ordering"]
