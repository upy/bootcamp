from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, BasketDetailedSerializer, AddToBasketSerializer

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

    """ Yorum satırları hatalı çalışıyor tekrar inceleyeceğim"""

    """print("deneme18", self.request.data)
        product_id = self.request.data['product']
        customer = self.request.data['customer']

        product = Product.objects.get(id=product_id)
        print("product: ", product)
        basket = self.request.data['basket']
        print("basket", basket)
        basketItem = BasketItem.objects.get_or_create(id=basket)
        print("basketitem", basketItem)
        print("quantity", self.request.data['quantity'])
        if basketItem.quantity in None:
            basketItem.quantity = self.request.data['quantity']
        else:
            basketItem.quantity = (basketItem.quantity + self.request.data['quantity'])
        basketItem.save()

        return Response(data="Item was added")


"""


""" #def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {"basket__customer__id": self.request.user.id}
        obj = get_object_or_404(queryset, **filter_kwargs)

        return obj """


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "add_to_basket": BasketItemSerializer
    }
    """ add_to_basket """
    @action(detail=False, methods=["post"])
    def add_to_basket(self, request, *args, **kwargs):
        user_id = self.request.user.id
        product = Product.objects.get(id=request.data["product"])
        quantity = request.data["quantity"]
        price = product.price
        basket = Basket.objects.filter(customer__id=user_id, status="open").first()
        if not basket:
            basket = Basket.objects.create(customer__id=user_id, status="open")

        basket_item = BasketItem.objects.filter(basket__customer__id=user_id, product=product,
                                                price=float(str(price))).first()

        if not basket_item:
            basket_item = BasketItem.objects.create(basket=basket, product=product, quantity=quantity,
                                                   price=float(str(price)))
        else:
            basket_item.quantity += float(quantity)
            basket_item.save()
        serializer_detailed_data = BasketItemDetailedSerializer(basket_item).data
        return Response(dict(serializer_detailed_data))


    """def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {"customer__id": self.request.user.id}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj"""
