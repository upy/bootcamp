from django.db.transaction import atomic
from rest_framework import serializers

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem
from customers.models import City, Country, Customer, Address


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityDetailedSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AddressDetailedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    city = CitySerializer()
    class Meta:
        model = Address
        fields = '__all__'
