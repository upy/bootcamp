from rest_framework import serializers

from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductDetailedSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("id", "customer", "status")


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price",)


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketDetailedSerializer()
    product = ProductDetailedSerializer()
