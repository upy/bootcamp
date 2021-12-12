from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin

from baskets.models import Basket, BasketItem
from baskets.filters import BasketFilter, BasketItemFilter
from baskets.serializers import BasketSerializers, BasketItemSerializers


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializers
    filterset_class = BasketFilter


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializers
    filterset_class = BasketItemFilter