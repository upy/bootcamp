from django.db.transaction import atomic
from rest_framework import serializers
from customers.models import Customer, Address, City, Country

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("customer", "name", "full_name", "line_1","line_2","phone","district","zipcode","city")


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ("name", )

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = ("name", "country")

class AddressDetailedSerializer(AddressSerializer):
    customer = CustomerSerializer()
    city = CitySerializer()


    @atomic()
    def create(self, validated_data):
        customers = validated_data.pop("customers", None)
        address = super().create(validated_data)
        if customers:
            serializer = CustomerSerializer(data=addresses, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            address.customers.add(*serializer.instance)
        return address


