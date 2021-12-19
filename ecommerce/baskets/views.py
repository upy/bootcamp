from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, BasketDetailedSerializer
from core.mixins import DetailedViewSetMixin


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(basket__customer__id=user)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "add_item_to_basket": BasketItemSerializer
    }

    @action(detail=True, methods=['post'])
    def add_item_to_basket(self, request, pk=None):
        serializer = BasketItemSerializer(data=request.data)
        serializer.save()

        return Response(serializer.data)