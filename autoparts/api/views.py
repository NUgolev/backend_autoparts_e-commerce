from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .filters import *
from rest_framework import filters


class ProductViewSet(ModelViewSet):
    """
    Вид для просмотра списка продуктов
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    pagination_class = None
    filterset_class = ProductFilter
    http_method_names = ["get"]

    @action(detail=False, methods=["GET"], url_path="max-min-price")
    def max_mix_price(self, request, **kwargs):
        """
        Получение минимальной и максимальной цены для продуктов подходящих под фильтрацию

        Можно фильтровать так же как и в GET api/product/
        """
        queryset = self.filter_queryset(self.get_queryset())
        return Response(
            {
                "min_price": min(queryset.values_list("price", flat=True), default=0),
                "max_price": max(queryset.values_list("price", flat=True), default=0),
            }
        )


class CategoryViewSet(ModelViewSet):
    """
    Вид для получения дерева категорий
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
    pagination_class = None
    filterset_class = CategoryFilter
    http_method_names = ["get"]

    @action(detail=True, methods=["GET"], url_path="children")
    def children(self, request, pk=None):
        """
        Получение детей категории
        """
        queryset = self.queryset.filter(parent__id=pk)
        return Response(self.serializer_class(queryset, many=True).data)


class ProductFilterViewSet(ModelViewSet):
    """
    Вид для просмотра списка продуктов
    """

    queryset = Filter.objects.all()
    serializer_class = ProductFilterSerializer
    permission_classes = []
    pagination_class = None
    filterset_class = ProductFilterFilter
    http_method_names = ["get"]


view_sets = [
    ("product", ProductViewSet),
    ("category", CategoryViewSet),
    ("filter", ProductFilterViewSet),
]
