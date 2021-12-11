from rest_framework import serializers
from django.db.transaction import atomic
from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer



class BasketSerializer(serializers.ModelSerializer):
    """
    Basket Serializer
    """

    class Meta:
        model = Basket
        fields = ("id", "customer", "status", "created_at", "modified_at")


class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketItemDetailedSerializer(BasketItemSerializer):
    """
    Basket Item Detailed Serializer
    """
    basket = BasketSerializer(many=False)

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")

    @atomic()
    def create(self, validated_data):
        basket = validated_data.pop("basket", None)
        basket_item = super().create(validated_data)

        if basket:
            serializer = BasketSerializer(data=basket, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket_item.basket.add(*serializer.instance)
        return basket_item


class BasketDetailedSerializer(BasketSerializer):
    """
    Basket Detailed Serializer
    """
    customer = CustomerSerializer(many=False)

    class Meta:
        model = Basket
        fields = ("id", "customer", "status", "created_at", "modified_at")

    @atomic()
    def create(self, validated_data):
        customer = validated_data.pop("customer", None)
        basket = super().create(validated_data)

        if basket:
            serializer = CustomerSerializer(data=customer, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket.customer.add(*serializer.instance)
        return basket
