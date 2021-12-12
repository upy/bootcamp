from django.db.transaction import atomic
from rest_framework import serializers

from baskets.serializers import BasketSerializer
from core.models import get_all_base_abstract_model_attrs
from customers.models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "name",


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "name", "city"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = get_all_customer_attrs() + ("id") + get_all_base_abstract_model_attrs


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("id",) + get_all_customer_attrs() + get_all_base_abstract_model_attrs()


class DetailedCustomerSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    baskets = BasketSerializer(many=True)

    class Meta:
        model = Address
        fields = ("id",) + get_all_customer_attrs() + get_all_base_abstract_model_attrs()


class DetailedAddressSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Address
        fields = ("id",) + get_all_customer_attrs() + get_all_base_abstract_model_attrs()
