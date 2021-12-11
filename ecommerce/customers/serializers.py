from rest_framework import serializers

from customers.models import City, Country, Customer, Address


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id', 'customer', 'name', 'full_name', 'line_1', 'line_2', 'phone', 'district', 'zipcode', 'city',
            'is_default')


class CityDetailedSerializer(CitySerializer):
    countries = CountrySerializer()


class AddressDetailedSerializer(AddressSerializer):
    customers = CustomerSerializer
    cities = CitySerializer
