from django.db.transaction import atomic
from rest_framework import serializers

from customers.serializers import CitySerializer, CustomerSerializer
from baskets.serializers import BasketSerializer
from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = '__all__'


class BillingAddressDetailedSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = BillingAddress
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class ShippingAddressDetailedSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    basket = BasketSerializer()
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()
    class Meta:
        model = Order
        fields = '__all__'


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = '__all__'


class OrderBankAccountDetailedSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = OrderBankAccount
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderItemDetailedSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'
