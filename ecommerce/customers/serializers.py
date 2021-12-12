from django.db.transaction import atomic
from rest_framework import serializers
from customers.models import Customer, City, Address, Country

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email",)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "country",)


class CityDetailedSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ("id", "name", "country",)

    @atomic()
    def create(self, validated_data):
        country = validated_data.pop("country", None)
        city = super().create(validated_data)
        if country:
            serializer = CountrySerializer(data=country)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            city.country.add(*serializer.instance)
        return city


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("id", "customer", "name", "full_name",
                  "line_1", "line_2", "phone", "district", "zipcode",
                  "city", "is_default")


class AddressDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    city = CityDetailedSerializer()

    class Meta:
        model = Address
        fields = ("id", "customer", "name", "full_name",
                  "line_1", "line_2", "phone", "district", "zipcode",
                  "city", "is_default")

    @atomic()
    def create(self, validated_data):
        customer = validated_data.pop("customer", None)
        city = validated_data.pop("city", None)

        address = super().create(validated_data)

        if customer:
            serializer = CustomerSerializer(data=customer)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            address.customer.add(*serializer.instance)

        address = super().create(validated_data)

        if city:
            serializer = CityDetailedSerializer(data=city)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            address.city.add(*serializer.instance)
        return address


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name",)