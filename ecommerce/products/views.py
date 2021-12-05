from rest_framework import viewsets

from products.filters import ProductFilter
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer, \
    ProductDetailedSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetailedViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related("categories").all()
    serializer_class = ProductDetailedSerializer
    http_method_names = ["get"]

