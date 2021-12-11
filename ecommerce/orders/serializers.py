from rest_framework import serializers

from baskets.serializers import BasketDetailedSerializer
from customers.serializers import CustomerSerializer, CityDetailedSerializer
from orders.models import BillingAddress, Order, ShippingAddress, OrderItem, \
    OrderBankAccount


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = (
            "id", "full_name", "line_1", "line_2", "phone", "district",
            "zipcode",
            "city",)

class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CityDetailedSerializer()

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            "id", "full_name", "line_1", "line_2", "phone", "district",
            "zipcode",
            "city",)

class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CityDetailedSerializer()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "billing_address", "shipping_address", "total_price", )

class OrderDetailedSerializer(OrderSerializer):
    customer = CustomerSerializer()
    basket = BasketDetailedSerializer()
    billing_address = BillingAddressDetailedSerializer()
    shipping_address = ShippingAddressDetailedSerializer()


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("order", "product", "price", )

class OrderItemDetailedSerializer(OrderItemSerializer):
    order = OrderDetailedSerializer()

class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")

class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderDetailedSerializer()
