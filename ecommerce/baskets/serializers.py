from django.db.transaction import atomic
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from baskets.models import BasketItem, Basket
from customers.serializers import CustomerSerializer
from products.models import Product
from products.serializers import ProductSerializer,ProductDetailedSerializer


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "customer", "product", "quantity", "price")


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ("id", "customer","status")


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketSerializer()
    product = ProductSerializer()


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()


class AddToBasketSerializer(serializers.ModelSerializer):
      product = ProductDetailedSerializer()
    #basketItem = BasketItemSerializer()

      class Meta:
        model = BasketItem
        fields = ("id", "basket", "customer","product", "quantity", "price")
