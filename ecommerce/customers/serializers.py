from rest_framework import serializers
from customers.models import Customer, City, Country, Address
from django.db.transaction import atomic



class CitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("id", "name", "country",)
        model = City

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ("id", "name", )

class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer(many= False)

    class Meta:
        model = City
        fields = ("id", "name", "country",)

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
    """
    Address Detailed Serializer
    includes Customer and DetailedCity Serializers
    """
    customer = CustomerSerializer(many=False)
    city = CityDetailedSerializer(many= False)

    class Meta:
        model = Address
        fields = ("id", "customer", "name", "full_name", "line_1", "line_2",
                  "phone", "district", "zipcode", "city")
    @atomic()
    def create(self, validated_data):
        customer = validated_data.pop("customer", None)
        address = super().create(validated_data)

        if customer:
            serializer = CustomerSerializer(data=customer, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            address.customer.add(*serializer.instance)

        city = validated_data.pop("city", None)
        address = super().create(validated_data)

        if city:
            serializer = CityDetailedSerializer(data=city, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            address.city.add(*serializer.instance)

        return address

