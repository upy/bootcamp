from django.db.transaction import atomic
from rest_framework import serializers

from orders.models import (BillingAddress, Order, OrderBankAccount,
                           OrderItem, ShippingAddress)
from customers.serializers import CustomerSerializer, CitySerializer
from baskets.serializers import BasketSerializer


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = '__all__'


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = '__all__'


class OrderDetailedSerializer(OrderSerializer):
    customer = CustomerSerializer()
    basket = BasketSerializer()
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()

    @atomic()
    def create(self, validated_data, order=None):
        customer = validated_data.pop('customer', None)
        basket = validated_data.pop('basket', None)
        billing_address = validated_data.pop('billing_address', None)
        shipping_address = validated_data.pop('shipping_address', None)

        order.super().create(validated_data)
        if customer:
            serializer = CustomerSerializer(data=customer)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order.customer.add(*serializer.instance)
        order = super().create(validated_data)

        if billing_address:
            serializer = BillingAddressSerializer(data=billing_address)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order.billing_address.add(*serializer.instance)
        order = super().create(validated_data)

        if shipping_address:
            serializer = ShippingAddressSerializer(data=shipping_address)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order.shipping_address.add(*serializer.instance)
        order = super().create(validated_data)

        if basket:
            serializer = BasketSerializer(data=basket, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order.basket.add(*serializer.instance)
        return order


class OrderItemDetailedSerializer(OrderItemSerializer):
    order = OrderSerializer()

    @atomic()
    def create(self, validated_data):
        order = validated_data.pop("order", None)
        order_item = super().create(validated_data)
        if order_item:
            serializer = OrderSerializer(data=order)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order_item.order.add(*serializer.instance)

        return order_item


class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CitySerializer()

    @atomic()
    def create(self, validated_data):
        city = validated_data.pop("city", None)
        billing_address = super().create(validated_data)
        if city:
            serializer = CitySerializer(data=city)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            billing_address.city.add(*serializer.instance)
        return billing_address


class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CitySerializer()

    @atomic()
    def create(self, validated_data):
        city = validated_data.pop("city", None)
        shipping_address = super().create(validated_data)
        if city:
            serializer = CitySerializer(data=city,)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            shipping_address.city.add(*serializer.instance)
        return shipping_address


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()

    @atomic()
    def create(self, validated_data):
        order = validated_data.pop("order", None)
        bank_account = super().create(validated_data)
        if order:
            serializer = CitySerializer(data=order,)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            bank_account.order.add(*serializer.instance)
        return bank_account

