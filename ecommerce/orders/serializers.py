from django.db.transaction import atomic
from rest_framework import serializers
from baskets.serializers import BasketSerializer
from customers.serializers import CitySerializer, CustomerSerializer
from orders.models import BillingAddress, ShippingAddress, Order, OrderBankAccount, OrderItem


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city",)


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city",)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order",)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "price",)


class BillingAddressDetailedSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False)

    class Meta:
        model = BillingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")

    @atomic()
    def create(self, validated_data):
        city = validated_data.pop("city", None)
        billing_address = super().create(validated_data)
        if city:
            serializer = CitySerializer(data=city, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            billing_address.city.add(*serializer.instance)
        return billing_address


class ShippingAddressDetailedSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False)

    class Meta:
        model = ShippingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city",)

    @atomic()
    def create(self, validated_data):
        city = validated_data.pop("city", None)
        shipping_address = super().create(validated_data)
        if city:
            serializer = CitySerializer(data=city, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            shipping_address.city.add(*serializer.instance)
        return shipping_address


class OrderItemDetailedSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False)

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "price",)

    @atomic()
    def create(self, validated_data):
        order = validated_data.pop("order", None)
        order_item = super().create(validated_data)
        if order_item:
            serializer = OrderSerializer(data=order, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order_item.order.add(*serializer.instance)

        return order_item


class OrderDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    basket = BasketSerializer(many=False)
    billing_address = BillingAddressSerializer(many=False)
    shipping_address = ShippingAddressSerializer(many=False)

    class Meta:
        model = Order
        fields = ("id", "customer", "basket", "status", "billing_address", "shipping_address", "total_price")

    @atomic()
    def create(self, validated_data):
        customer = validated_data.pop("customer", None)
        basket = validated_data.pop("basket", None)

        order = super().create(validated_data)
        if customer:
            serializer = CustomerSerializer(data=customer, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order.customer.add(*serializer.instance)

        order = super().create(validated_data)
        if basket:
            serializer = BasketSerializer(data=basket, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            order.basket.add(*serializer.instance)
        return order


class OrderBankAccountDetailedSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False)

    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order",)

    @atomic()
    def create(self, validated_data):
        order = validated_data.pop("order", None)
        bank_account = super().create(validated_data)
        if order:
            serializer = OrderSerializer(data=order, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            bank_account.order.add(*serializer.instance)

        return bank_account