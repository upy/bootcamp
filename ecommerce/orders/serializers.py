from rest_framework import serializers

from customers.serializers import CitySerializer, CustomerSerializer
from orders.models import ShippingAddress, BillingAddress, OrderBankAccount, Order, OrderItem


# Billing Address Serializer
class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ('id', 'full_name', 'line_1', 'line_2', 'phone', 'district', 'zipcode', 'city')


# Shipping Address Serializer
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ('id', 'full_name', 'line_1', 'line_2', 'phone', 'district', 'zipcode', 'city')


# Order Bank Account Serializer
class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = ('id', 'name', 'iban', 'bank_name', 'order')


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'basket', 'status', 'billing_address', 'shipping_address', 'total_price')


# Order Item Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price')


# Billing Address Detailed Serializer - nested serializer
class BillingAddressDetailedSerializer(BillingAddressSerializer):
    cities = CitySerializer()


# Shipping Address Detailed Serializer - nested serializer
class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    cities = CitySerializer()


# Order Bank Account Detailed Serializer - nested serializer
class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    orders = OrderSerializer()


# Order Detailed Serializer - nested serializer
class OrderDetailedSerializer(OrderSerializer):
    customers = CustomerSerializer()
    billing_addresses = BillingAddressSerializer()
    shipping_addresses = ShippingAddressSerializer()


# Order Item Detailed Serializer - nested serializer
class OrderItemDetailedSerializer(OrderItemSerializer):
    orders = OrderSerializer()
