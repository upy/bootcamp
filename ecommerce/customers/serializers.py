from rest_framework import serializers

from customers.models import Country, City, Customer, Address


class NestedCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name",)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name", "created_at", "modified_at")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "country", "created_at", "modified_at")


class CityDetailedSerializer(serializers.ModelSerializer):

    country = NestedCountrySerializer()

    class Meta:
        model = City
        fields = ("id", "name", "country", "created_at", "modified_at")


class NestedCitySerializer(serializers.ModelSerializer):
    country = NestedCountrySerializer()

    class Meta:
        model = City
        fields = ("id", "name", "country")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id", "customer", "name", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city",
            "is_default", "created_at", "modified_at")


class AddressDetailedSerializer(serializers.ModelSerializer):

    city = NestedCitySerializer()

    class Meta:
        model = Address
        fields = (
            "id", "customer", "name", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city",
            "is_default", "created_at", "modified_at")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "date_joined")
