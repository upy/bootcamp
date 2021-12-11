from rest_framework import viewsets

from baskets.serializers import BasketSerializer, BasketItemSerializer
from baskets.models import Basket, BasketItem


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer