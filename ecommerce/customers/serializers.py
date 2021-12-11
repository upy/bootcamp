from rest_framework import serializers

from customers.models import City, Country, Customer, Address


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ("name", )


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ("name", "country")


class CityDetailedSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ("name", "country")


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "is_staff", "is_active", "date_joined")


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("customer", "name", "full_name", "line_1", "line_2", "phone", "district",
                  "zipcode", "city", "is_default")


class AddressDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    city = CityDetailedSerializer()

    class Meta:
        model = Address
        fields = ("customer", "name", "full_name", "line_1", "line_2", "phone", "district",
                  "zipcode", "city", "is_default")




