from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.transaction import atomic
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, \
    BasketDetailedSerializer
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
        user = self.request.user
        return queryset.filter(basket__customer__id=user)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)

    @atomic()
    @action(detail=True, methods=['post'], http_method_names=['post'])
    def add_basket_item(self, request):

        user_id = self.request.user.id
        product = Product.objects.get(id=request.data["product"])
        quantity = request.data["quantity"]
        price = product.price

        try:
            basket = Basket.objects.get(customer__id=user_id)
        except ObjectDoesNotExist:
            basket = Basket.objects.create(customer_id=user_id)
        except MultipleObjectsReturned:
            basket = Basket.objects.filter(customer__id=user_id).first()

        basket_item = BasketItem.objects.filter(basket=basket, product=product, price=price).first()

        if basket_item:
            basket_item.quantity += quantity

        else:
            basket_item = BasketItem.objects.create(basket=basket, product=product, quantity=quantity,price=price)

        basket_item.save()
        basket.save()

        serializer = BasketItemSerializer(basket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
