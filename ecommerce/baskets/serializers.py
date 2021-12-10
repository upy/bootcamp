from django.db.transaction import atomic
from rest_framework import serializers

from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer, ProductDetailedSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("id", "customer", "status")


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)

    class Meta:
        model = Basket
        fields = ("customer", "status")

    @atomic()
    def create(self, validated_data):
        customer = validated_data.pop("customer", None)
        basket = super().create(validated_data)
        if customer:
            serializer = CustomerSerializer(data=customer, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket.customer.add(*serializer.instance)
        return basket


class BasketItemDetailedSerializer(serializers.ModelSerializer):
    basket = BasketDetailedSerializer(many=False)
    product = ProductDetailedSerializer(many=False)

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")

    @atomic()
    def create(self, validated_data):
        basket = validated_data.pop("basket", None)
        product = validated_data.pop("product", None)

        basket_item = super().create(validated_data)

        if basket:
            serializer = BasketSerializer(data=basket, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket_item.basket.add(*serializer.instance)

        basket_item = super().create(validated_data)

        if product:
            serializer = ProductSerializer(data=product, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket_item.product.add(*serializer.instance)
        return basket_item
