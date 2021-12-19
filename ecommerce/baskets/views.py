from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, \
    BasketDetailedSerializer, AddBasketItemSerializer
from core.mixins import DetailedViewSetMixin


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
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
        print(queryset.filter(basket__customer=user))
        return queryset.filter(basket__customer=user)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "add_basket_item": AddBasketItemSerializer
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)

    @action(detail=True, methods=["post"])
    def add_basket_item(self, request, pk):
            copy_data = request.data.copy()
            copy_data["basket_id"] = pk
            serializer = BasketItemSerializer(data=copy_data)
            if serializer.is_valid():
                BasketItem.create(copy_data)
            return Response(serializer.data)
