from rest_framework import serializers

from baskets.serializers import BasketDetailedSerializer
from customers.serializers import CustomerSerializer, CityDetailedSerializer
from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem


class BillingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class BillingAddressDetailedSerializer(serializers.ModelSerializer):
    city = CityDetailedSerializer()

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressDetailedSerializer(serializers.ModelSerializer):
    city = CityDetailedSerializer()

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class OrderDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    basket = BasketDetailedSerializer()
    billing_address = BillingAddressDetailedSerializer()
    shipping_address = ShippingAddressDetailedSerializer()

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class OrderBankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")


class OrderBankAccountDetailedSerializer(serializers.ModelSerializer):
    order = OrderDetailedSerializer()

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")


class OrderItemDetailedSerializer(serializers.ModelSerializer):
    order = OrderDetailedSerializer()

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")


