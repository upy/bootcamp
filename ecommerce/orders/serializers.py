from rest_framework import serializers

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem
from customers.serializers import CitySerializer, CustomerSerializer
from baskets.serializers import BasketSerializer


class BillingAddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    basket = BasketSerializer()
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class OrderBankAccountSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")