from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from baskets.filters import BasketFilter
from baskets.models import Basket, BasketItem
from baskets.serializers import BasketSerializer, BasketItemSerializer, BasketItemDetailedSerializer

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter

class BasketItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

class BasketItemDetailedViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemDetailedSerializer
    http_method_names = ["get"]