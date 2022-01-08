from rest_framework import serializers
from core.mixins import DetailedViewSetMixin

from customers.models import Customer, Address, City, Country


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name",)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ("id", "name", "country")


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "name", "full_name", "phone", "district", "zipcode", "city", "customer")


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()


class AddressDetailedSerializer(AddressSerializer):
    customer = CustomerSerializer()
    city = CitySerializer()




