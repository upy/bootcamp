from rest_framework import serializers

from customers.serializers import CustomerSerializer, CitySerializer
from orders.models import  BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem


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
        fields = ("id", "name")

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "order", "product", "price")

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "customer", "basket", "status", "billing_address", "shipping_address", "total_price")

class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CitySerializer()

class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CitySerializer()

class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()

class OrderDetailedSerializer(OrderSerializer):
    customer = CustomerSerializer()
    # basket = BasketSerializer() # not implemented yet
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()

class OrderItemDetailedSerializer(OrderItemSerializer):
    order = OrderSerializer()


