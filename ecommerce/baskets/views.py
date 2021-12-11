from rest_framework import viewsets

from baskets.filters import BasketFilter
from core.mixins import DetailedViewSetMixin
from baskets.serializers import *


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    """
    Detailed ViewSet for Basket
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter  # TODO: basket için filter ekle
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
    }


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    """
    Detailed ViewSet for BasketItem
    """
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketFilter  # TODO: basketitem için filter ekle
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }