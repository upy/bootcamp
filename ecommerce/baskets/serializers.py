from django.db.transaction import atomic
from rest_framework import serializers

from baskets.models import Basket, BasketItem

from products.serializers import ProductSerializer, ProductDetailedSerializer
from customers.serializers import CustomerSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = ("id", "customer", "status")


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = ("id", "basket", "product", "quantity", "price")


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Basket
        fields = ("customer", "status")

    @atomic()
    def create(self, validated_data):
        customer = validated_data.pop("customer", None)
        basket = super().create(validated_data)

        if customer:
            serializer = CustomerSerializer(data=customer)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket.customer.add(*serializer.instance)

        return basket


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketDetailedSerializer()
    product = ProductDetailedSerializer()

    @atomic()
    def create(self, validated_data):
        basket = validated_data.pop("basket", None)
        product = validated_data.pop("product", None)

        basket_item = super().create(validated_data)

        if basket:
            serializer = BasketSerializer(data=basket)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket_item.basket.add(*serializer.instance)
        if product:
            serializer = ProductSerializer(data=product)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            basket_item.product.add(*serializer.instance)
        return basket_item