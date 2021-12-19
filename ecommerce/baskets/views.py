from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, BasketDetailedSerializer
from core.mixins import DetailedViewSetMixin


class BasketItemViewSet(DetailedViewSetMixin,viewsets.ModelViewSet):
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
        user = self.request.user.id
        return queryset.filter(basket__customer__id=user)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = ()
    http_method_names = ["get", "delete", "post"]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "create_product": BasketItemSerializer
    }

    def get_queryset(self):
        # customer can only see own basket
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)

    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        serializer = BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
