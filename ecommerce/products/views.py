from rest_framework import viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet

from core.mixins import DetailedViewSetMixin
from core.utils import IsStaffUserAuthenticated
from products.filters import ProductFilter, PriceFilter
from products.models import Product, Category, Price
from products.serializers import ProductSerializer, CategorySerializer, \
    ProductDetailedSerializer, PriceSerializer


class ProductViewSet(DetailedViewSetMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, GenericViewSet):
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": ProductDetailedSerializer,
        "detailed": ProductDetailedSerializer,
    }


class AdminProductViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
        IsStaffUserAuthenticated
    )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": ProductDetailedSerializer,
        "detailed": ProductDetailedSerializer,
    }


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    http_method_names = ["get"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PriceViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    http_method_names = ["get"]
    queryset = Price.objects.all()
    filterset_class = PriceFilter
    serializer_class = PriceSerializer
