from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from baskets.models import Basket, BasketItem
from products.serializers import NestedProductSerializer


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price", "created_at", "modified_at")


class NestedBasketItemDetailed(serializers.ModelSerializer):

    product = NestedProductSerializer()

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("id", "customer", "status", "created_at", "modified_at")


class BasketDetailedSerializer(serializers.ModelSerializer):
    items = SerializerMethodField()

    def get_items(self, obj):
        basket_item_qset = BasketItem.objects.filter(basket__id=obj.id)

        items = NestedBasketItemDetailed(basket_item_qset, many=True).data
        return items

    class Meta:
        model = Basket
        fields = ("id", "customer", "status", "items", "created_at", "modified_at")
