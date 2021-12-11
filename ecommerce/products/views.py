from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from products.filters import PriceFilter, ProductFilter, StockFilter
from products.models import Price, Product, Category, Stock
from products.serializers import PriceDetailedSerializer, PriceSerializer, ProductSerializer, CategorySerializer, \
    ProductDetailedSerializer, StockDetailedSerializer, StockSerializer


class ProductViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": ProductDetailedSerializer,
        "detailed": ProductDetailedSerializer,
    }


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StockViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_class = StockFilter
    serializer_action_classes = {
        "detailed_list": StockDetailedSerializer,
        "detailed": StockDetailedSerializer,
    }

class PriceViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filterset_class = PriceFilter
    serializer_action_classes = {
        "detailed_list": PriceDetailedSerializer,
        "detailed": PriceDetailedSerializer,
    }
