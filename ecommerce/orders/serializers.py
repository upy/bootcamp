from rest_framework import serializers

from core.models import get_all_base_abstract_model_attrs
from customers.serializers import CustomerSerializer
from orders.models import *


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = get_all_billing_address_attrs() + get_all_base_abstract_model_attrs() + "id"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = get_all_shipping_address_attrs() + get_all_base_abstract_model_attrs() + "id"


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = get_all_order_bank_account_attrs() + get_all_base_abstract_model_attrs() + "id"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = get_all_order_attrs() + get_all_base_abstract_model_attrs() + "id"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = get_all_order_item_attrs() + get_all_base_abstract_model_attrs() + "id"


class OrderBankAccountDetailedSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderBankAccount
        fields = get_all_order_bank_account_attrs() + get_all_base_abstract_model_attrs() + "id"


class OrderDetailedSerializer(serializers.ModelSerializer):
    order_bank_accounts = OrderBankAccountSerializer(many=True)
    customer = CustomerSerializer()
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = get_all_order_attrs() + get_all_base_abstract_model_attrs() + "id"


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderItem
        fields = get_all_order_item_attrs() + get_all_base_abstract_model_attrs() + "id"
