from rest_framework import serializers

from orders.models import Order, OrderItem, OrderBankAccount, ShippingAddress, BillingAddress

class BillingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone","district", "zipcode", "city")

class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone","district", "zipcode", "city")

class OrderBankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("customer", "basket","status","billing_address", "shipping_address","total_price" )


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("order", "product","price" )

class OrderDetailedSerializer(OrderSerializer):
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()