from rest_framework import serializers
from django.db.transaction import atomic
from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    """
    Basket Serializer
    """

    class Meta:
        model = Basket
        fields = ("id", "customer", "status", "created_at", "modified_at")


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketItemDetailedSerializer(BasketItemSerializer):
    """
    Basket Item Detailed Serializer
    """
    basket = BasketSerializer(many=False)


class BasketDetailedSerializer(BasketSerializer):
    """
    Basket Detailed Serializer
    """
    customer = CustomerSerializer(many=False)

