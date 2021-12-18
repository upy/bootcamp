from decimal import Decimal

from django.db.transaction import atomic
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, \
    BasketItemDetailedSerializer, BasketDetailedSerializer
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
    # lookup_field = 'basket'
    permission_classes = ()
    http_method_names = ["get", "delete"]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "add_basket_item": BasketItemSerializer,
        "get_basket_items": BasketItemSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)

    @action(detail=False, methods=['get'], http_method_names=['get'])
    def get_basket_items(self, request):
        """
        An endpoint to show all items under the basket.
        """
        user = self.request.user
        basket_items_list = self.get_queryset().filter(
            customer__id=user.id).first().basketitem_set.all()
        serializer = self.get_serializer(basket_items_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], http_method_names=['post'])
    @atomic()
    def add_basket_item(self, request, pk=None):
        """
        Adds an item to the basket and updates stocks.
        """
        pk = None
        user = self.request.user

        basket = self.get_object()
        try:
            product = Product.objects.get(id=request.data["product"])
            quantity = int(request.data["quantity"])
            price = Decimal(request.data["price"])
        except Exception as e:
            return Response({'status': 'fail'})

        stock = product.stock
        if stock.quantity <= 0 or stock.quantity < quantity:
            return Response({'status': 'fail'})

        item_in_basket = BasketItem.objects.filter(basket=basket,
                                                   product=product,
                                                   price=price).first()
        if item_in_basket:
            item_in_basket.quantity += quantity
            stock.quantity -= quantity
            stock.save()
            item_in_basket.save()
        else:
            new_item = BasketItem(basket=basket, product=product,
                                  quantity=quantity, price=price)
            stock.quantity -= quantity
            stock.save()
            new_item.save()

        serializer = BasketSerializer(basket)
        return Response(serializer.data, status=status.HTTP_200_OK)
