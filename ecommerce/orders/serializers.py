from django.db.transaction import atomic
from rest_framework import serializers

from baskets.serializers import BasketSerializer
from customers.serializers import CitySerializer, CustomerSerializer
from orders.models import *


class BillingAddressSerializer(serializers.ModelSerializer):
    """
    Billing Address Serializer
    """
    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressSerializer(serializers.ModelSerializer):
    """
    Shipping Address Serializer
    """
    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderSerializer(serializers.ModelSerializer):
    """
    Order Serializer
    """
    class Meta:
        model = Order
        fields = ["customer", "basket", "status", "billing_address", "shipping_address", "total_price"]


class OrderBankAccountSerializer(serializers.ModelSerializer):
    """
    Order Bank Account Serializer
    """
    class Meta:
        model = OrderBankAccount
        fields = ["name", "iban", "bank_name", "order"]


class BillingAddressDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Billing Address Serializer
    """
    city = CitySerializer

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Shipping Address Serializer
    """
    city = CitySerializer

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Order Serializer
    """
    customer = CustomerSerializer
    basket = BasketSerializer
    billing_address = BillingAddressSerializer
    shipping_address = ShippingAddressSerializer

    class Meta:
        model = Order
        fields = ["customer", "basket", "status", "billing_address", "shipping_address", "total_price"]


class OrderBankAccountDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Order Bank Account Serializer
    """
    order = OrderSerializer

    class Meta:
        model = OrderBankAccount
        fields = ["name", "iban", "bank_name", "order"]