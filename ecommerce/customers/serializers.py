from rest_framework import serializers

from customers.models import City, Country, Customer, Address


# City Serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country')


# Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')


# Address Serializer
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id', 'customer', 'name', 'full_name', 'line_1', 'line_2', 'phone', 'district', 'zipcode', 'city',
            'is_default')


# City Detailed Serializer - nested serializer
class CityDetailedSerializer(CitySerializer):
    countries = CountrySerializer()


# Address Detailed Serializer - nested serializer
class AddressDetailedSerializer(AddressSerializer):
    customers = CustomerSerializer
    cities = CitySerializer
