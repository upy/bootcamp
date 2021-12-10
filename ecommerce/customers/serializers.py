from rest_framework import serializers
from customers.models import Customer, Country, City, Address


class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer Serializer
    """
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email"]


class CountrySerializer(serializers.ModelSerializer):
    """
    Country Serializer
    """
    class Meta:
        model = Country
        fields = ["name"]


class CitySerializer(serializers.ModelSerializer):
    """
    City Serializer
    """
    class Meta:
        model = City
        fields = ["name", "country"]


class AddressSerializer(serializers.ModelSerializer):
    """
    Address Serializer
    """
    class Meta:
        model = Address
        fields = ["customer", "name", "full_name", "line1", "line2", "phone", "district", "zipcode", "city",
                  "is_default"]


class AddressDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Address Serializer
    """
    customer = CustomerSerializer()
    city = CitySerializer()

    class Meta:
        model = Address
        fields = ["customer", "name", "full_name", "line1", "line2", "phone", "district", "zipcode", "city",
                  "is_default"]
