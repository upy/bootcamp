from django.db.transaction import atomic
from rest_framework import serializers

from customers.models import Customer, Address

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "name", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city", "is_default")