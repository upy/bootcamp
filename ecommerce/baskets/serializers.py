from django.db.transaction import atomic
from rest_framework import serializers

from baskets.models import Basket, BasketItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class BasketDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Basket
        fields = '__all__'

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'


class BasketItemDetailedSerializer(serializers.ModelSerializer):
    basket = BasketSerializer()
    product = ProductSerializer()
    class Meta:
        model = BasketItem
        fields = '__all__'
