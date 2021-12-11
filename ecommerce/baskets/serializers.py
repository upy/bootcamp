from rest_framework import serializers

from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer


# Basket Serializer
class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id', 'customer', 'status')


# Basket Detailed Serializer - nested serializer
class BasketDetailedSerializer(BasketSerializer):
    customers = CustomerSerializer()


# Basket Item Serializer
class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('id', 'basket', 'product', 'quantity', 'price')


# Basket Item Detailed Serializer - nested serializer
class BasketItemDetailedSerializer(BasketItemSerializer):
    baskets = BasketSerializer()
    products = ProductSerializer()
