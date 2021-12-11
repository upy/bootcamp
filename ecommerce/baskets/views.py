from django.shortcuts import render

from rest_framework import viewsets

from baskets.models import Basket
from baskets.serializers import BasketDetailedSerializer, BasketSerializer
from core.mixins import DetailedViewSetMixin


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detail": BasketDetailedSerializer,
    }

