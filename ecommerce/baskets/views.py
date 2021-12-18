from django.core.exceptions import ObjectDoesNotExist
from django.db.transaction import atomic
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, BasketDetailedSerializer
from core.mixins import DetailedViewSetMixin
from products.models import Product


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
        user_id = self.request.user.id
        return queryset.filter(basket__customer__id=user_id)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "delete"]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "add_to_basket": BasketItemSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)

    @atomic()
    @action(detail=True, methods=['post'], http_method_names=['post'])
    def add_to_basket(self, request, pk=None):
        user_id = self.request.user.id
        product = Product.objects.get(id=request.data["product"])
        quantity = request.data["quantity"]
        price = product.price
        try:
            basket = Basket.objects.get(customer__id=user_id, status="open")
        except ObjectDoesNotExist:
            basket = Basket.objects.create(customer_id=user_id, status="open")

        try:
            basket_item = BasketItem.objects.get(basket__customer__id=user_id, product=product)
            basket_item.quantity += int(quantity)
        except ObjectDoesNotExist:
            basket_item = BasketItem.objects.create(basket=basket, product=product, quantity=int(quantity), price=price)

        basket.save()
        basket_item.save()

        serializer = BasketItemSerializer(basket_item)
        return Response(serializer.data)
