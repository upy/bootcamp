from rest_framework import serializers
from orders.models import Order, OrderBankAccount, OrderItem, \
    BillingAddress, ShippingAddress
from baskets.models import Basket
from customers.models import City, Customer, Country
from baskets.serializers import BasketSerializer
from orders.managers import BillingAddressQuerySet, OrderQuerySet, \
    OrderItemQuerySet, OrderBankAccountQuerySet, ShippingAddressQuerySet


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "country")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name",)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "email")


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = (
            "id", "full_name", "line_1", "line_2", "phone", "district",
            "zipcode", "city")


class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CityDetailedSerializer()


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            "id", "full_name", "line_1", "line_2", "phone", "district",
            "zipcode", "city")


class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CityDetailedSerializer()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "customer", "basket", "status", "billing_address",
                  "shipping_address", "total_price")


class OrderDetailedSerializer(OrderSerializer):
    customer = CustomerSerializer()
    basket = BasketSerializer()


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order")


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "order", "product")


class OrderItemDetailedSerializer(OrderItemSerializer):
    order = OrderSerializer()
