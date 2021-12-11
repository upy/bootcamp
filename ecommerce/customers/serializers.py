from rest_framework import serializers

from core.mixins import DetailedViewSetMixin
from customers.models import Customer, Country, City, Address


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name", )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name", "country", )


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("name", "full_name","phone","district","zipcode","customer","city")


class AddressDetailedSerializer(AddressSerializer):
    city = CityDetailedSerializer()
    customer = CustomerSerializer()
