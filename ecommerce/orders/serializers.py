from django.db.transaction import atomic
from rest_framework import serializers
from customers.serializers import CustomerSerializer
from orders.models import Order, OrderItem, OrderBankAccount, BillingAddress, \
    ShippingAddress
from products.serializers import ProductSerializer

class BillingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone",
                  "district", "zipcode", "city")

class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone",
                  "district", "zipcode", "city")

class OrderBankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order")

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "billing_address",
                  "shipping_address", "total_price","created_at","modified_at")

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")

class OrderItemDetailedSerializer(serializers.ModelSerializer):
    """
    Order Item Detailed Serializer
    Order and Product Informations Included
    """
    order = OrderSerializer(many=False)
    product = ProductSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")

    @atomic()
    def create(self, validated_data):
        order = validated_data.pop("order", None)
        product = validated_data.pop("product", None)
        order_item = super().create(validated_data)

        if order:
            serializer = OrderSerializer(data=order, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order_item.order.add(*serializer.instance)

        if product:
            serializer = ProductSerializer(data=product, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order_item.order.add(*serializer.instance)

        return order
