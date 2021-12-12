from rest_framework import serializers

from baskets.models import *
from customers.serializers import CustomerSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "id", "customer", "status", "created_at", "modified_at"


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = "id", "basket", "product", "quantity", "price"


class BasketDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    basket_items = BasketSerializer(many=True)

    class Meta:
        model = Basket
        fields = "id", "customer", "status", "created_at", "modified_at"


class BasketItemDetailedSerializer(serializers.ModelSerializer):
    basket = BasketSerializer()

    class Meta:
        model = BasketItem
        fields = "id", "basket", "product", "quantity", "price"
