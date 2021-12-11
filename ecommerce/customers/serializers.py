from django.db.transaction import atomic
from rest_framework import serializers

from customers.models import Customer, Address, Country, City


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = ("first_name", "last_name", "email", "is_staff", "is_superuser")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = ("name",)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = ("name", "country",)


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()

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
        fields = "__all__"


class AddressDetailedSerializer(AddressSerializer):
    customer = CustomerSerializer()
    city = CityDetailedSerializer()

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
