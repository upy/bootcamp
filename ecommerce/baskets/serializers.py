from rest_framework import serializers
from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    """
    Basket Serializer
    """
    class Meta:
        model = Basket
        fields = ["customer", "status"]


class BasketItemSerializer(serializers.ModelSerializer):
    """
    Basket Item Serializer
    """
    class Meta:
        model = BasketItem
        fields = ["basket", "product", "quantity", "price"]


class BasketDetailedSerializer(serializers.ModelSerializer):
    """
    Basket Detailed Serializer for Customer
    """
    customer = CustomerSerializer()  # TODO: Add Customer Serializer!

    class Meta:
        model = Basket
        fields = ["customer", "status"]


class BasketItemDetailedSerializer(serializers.ModelSerializer):
    """
    Basket Item Detailed Serializer for Product and Basket
    """
    basket = BasketSerializer()
    product = ProductSerializer()

    class Meta:
        model = BasketItem
        fields = ["basket", "product", "quantity", "price"]