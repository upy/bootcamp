from rest_framework import serializers

from baskets.models import Basket, BasketItem
from customers.models import Customer
from baskets.managers import BasketItemQuerySet, BasketQuerySet
from products.serializers import ProductSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "email")


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("id", "customer", "status")
        manager = BasketQuerySet.as_manager()


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketSerializer()
    product = ProductSerializer()