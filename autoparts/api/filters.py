import json

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
    price_gte = django_filters.NumberFilter(
        field_name="price", lookup_expr="gte", label="Фильтрация по цене (больше чем)"
    )
    price_lte = django_filters.NumberFilter(
        field_name="price", lookup_expr="lte", label="Фильтрация по цене (меньше чем)"
    )
    category = django_filters.NumberFilter(
        method="category_filter", label="Поиск id категории"
    )
    ordering = django_filters.OrderingFilter(
        fields=(
            ("price", "price"),
            ("id", "id"),
        ),
        label="Сортировка по цене или новизне",
    )
    search = django_filters.CharFilter(
        method="search_filter", label="Поиск по названию/описанию"
    )
    filter = django_filters.CharFilter(
        method="prop_filter", label="Поиск по общим свойствам продуктов"
    )

    def prop_filter(self, queryset, name, value):
        filtered_queryset = queryset
        filter_json = json.loads(value)
        for filter_name in filter_json.keys():
            filter_list = filter_json.get(filter_name)
            if len(filter_list) == 0:
                continue
            filtered_queryset = filtered_queryset.filter(
                filter_values__filter__name=filter_name,
                filter_values__value__in=filter_list,
            )
        return filtered_queryset

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )

    def category_filter(self, queryset, name, value):
        where = f"product.category_id = any(get_children({value}))"
        return queryset.extra(where=[where])

    class Meta:
        model = Product
        fields = ["price_gte", "price_lte", "category", "ordering"]
