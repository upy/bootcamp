from rest_framework import serializers
from customers.models import Country, City, Address, Customer
from customers.managers import CustomerManager


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name", "country")


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "is_staff",
                  "is_active","date_joined")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("customer", "name",
                  "full_name", "line_1", "line_2", "phone", "district",
                  "zipcode", "city", "is_default")


class AddressDetailedSerializer(AddressSerializer):
    customer = CustomerSerializer()
    city = CitySerializer()
