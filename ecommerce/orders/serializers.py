from rest_framework import serializers

from customers.serializers import CustomerSerializer
from orders.models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "customer", "basket", "status", "total_price",)


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "product", "price", "order")


class OrderItemDetailedSerializer(OrderItemSerializer):

    order = OrderSerializer()


class OrderDetailedSerializer(OrderSerializer):

#    basket = BasketSerializer()
    customer = CustomerSerializer()