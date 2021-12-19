from rest_framework import serializers

from baskets.models import BasketItem, Basket
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer, ProductDetailedSerializer


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ("id", "customer", "status")


class BasketItemDetailedSerializer(BasketItemSerializer):
    product = ProductDetailedSerializer()


class BasketDetailedSerializer(BasketSerializer):
    basketitem_set = BasketItemDetailedSerializer(many=True)

    class Meta(BasketSerializer.Meta):
        fields = BasketSerializer.Meta.fields + ("basketitem_set", )
