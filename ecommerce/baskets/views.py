from django.shortcuts import render

from rest_framework import viewsets

from baskets.models import Basket, BasketItem
from baskets.serializers import BasketDetailedSerializer, BasketSerializer, \
    BasketItemSerializer, BasketItemDetailedSerializer
from core.mixins import DetailedViewSetMixin


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detail": BasketDetailedSerializer,
    }


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detail": BasketItemDetailedSerializer,
    }
