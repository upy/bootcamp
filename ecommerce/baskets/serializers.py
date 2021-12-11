from rest_framework import serializers

from baskets.models import Basket, BasketItem


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")