from rest_framework import serializers

from products.serializers import ProductSerializer
from customers.serializers import CustomerSerializer
from baskets.models import BasketItem, Basket


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ("id", "customer", "status")


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price",)


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketSerializer()
    product = ProductSerializer()


