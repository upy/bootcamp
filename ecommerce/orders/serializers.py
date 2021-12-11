from rest_framework import serializers

from orders.models import Order, ShippingAddress, BillingAddress, OrderBankAccount, OrderItem


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = (
            "id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city", "created_at", "modified_at")


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            "id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city", "created_at", "modified_at")


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order", "created_at", "modified_at")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id", "customer", "basket", "status", "billing_address", "shipping_address", "total_price", "created_at",
            "modified_at")


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "price", "created_at", "modified_at")
