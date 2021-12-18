from rest_framework import serializers

from baskets.serializers import BasketSerializer
from customers.serializers import CustomerSerializer, CitySerializer
from orders.models import OrderItem, Order, BillingAddress, ShippingAddress, OrderBankAccount


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "price")


class OrderSerializer(serializers.ModelSerializer):

    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ("id", "customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class BillingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderBankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order")


class OrderItemDetailedSerializer(OrderItemSerializer):
    order = OrderSerializer()


class OrderDetailedSerializer(OrderSerializer):
    customer = CustomerSerializer()
    basket = BasketSerializer()
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()


class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CitySerializer()


class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CitySerializer()

