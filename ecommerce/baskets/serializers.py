from rest_framework import serializers
from baskets.models import BasketItem, Basket
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Basket
        fields = ("id", "customer", "status")


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketSerializer()
    product = ProductSerializer()


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()
