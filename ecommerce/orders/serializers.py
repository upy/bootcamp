from rest_framework import serializers

from customers.serializers import CitySerializer, CustomerSerializer
from orders.models import ShippingAddress, BillingAddress, OrderBankAccount, Order, OrderItem


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ('id', 'full_name', 'line_1', 'line_2', 'phone', 'district', 'zipcode', 'city')


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ('id', 'full_name', 'line_1', 'line_2', 'phone', 'district', 'zipcode', 'city')


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = ('id', 'name', 'iban', 'bank_name', 'order')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'basket', 'status', 'billing_address', 'shipping_address', 'total_price')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price')


class BillingAddressDetailedSerializer(BillingAddressSerializer):
    cities = CitySerializer()


class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    cities = CitySerializer()


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    orders = OrderSerializer()


class OrderDetailedSerializer(OrderSerializer):
    customers = CustomerSerializer()
    billing_addresses = BillingAddressSerializer()
    shipping_addresses = ShippingAddressSerializer()


class OrderItemDetailedSerializer(OrderItemSerializer):
    orders = OrderSerializer()
