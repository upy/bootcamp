from django.db.transaction import atomic
from rest_framework import serializers

from baskets.models import Basket, BasketItem


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'
