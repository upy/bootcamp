from rest_framework import serializers

from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductDetailedSerializer


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")


class BasketItemDetailedSerializer(serializers.ModelSerializer):
    basket = BasketDetailedSerializer()
    product = ProductDetailedSerializer()

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")
