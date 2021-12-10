from rest_framework import serializers
from django.db.transaction import atomic

from customers.models import Customer, Address, City, Country


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "country")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("id", "customer", "name", "full_name", "line_1", "line_2",
                  "phone", "district", "zipcode", "city")


class AddressDetailedSerializer(AddressSerializer):
    customer = CustomerSerializer()
    city = CitySerializer()


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ("id", "name", "country")

        @atomic()
        def create(self, validated_data):
            country = validated_data.pop("country", None)
            city = super().create(validated_data)
            if country:
                serializer = CountrySerializer(data=country, many=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                city.categories.add(*serializer.instance)
            return city
