from rest_framework import serializers

from baskets.models import BasketItem, Basket
from customers.serializers import CustomerSerializer
from products.serializers import ProductDetailedSerializer, ProductSerializer


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")
        read_only_fields = ["basket", "price"]


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ("id", "customer", "status")


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketSerializer()
    product = ProductDetailedSerializer()


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()
