from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from baskets.filters import BasketFilter, BasketItemFilter
from baskets.models import Basket, BasketItem
from baskets.serializers import BasketSerializer, BasketDetailedSerializer, \
    BasketItemSerializer, BasketItemDetailedSerializer


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
    }


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }
