from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from products.filters import ProductFilter
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer, \
    ProductDetailedSerializer
from products.managers import ProductQuerySet


class ProductViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    manager_class = ProductQuerySet
    queryset = Product.objects.action_detailed_list()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": ProductDetailedSerializer,
        "detailed": ProductDetailedSerializer,
    }


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
