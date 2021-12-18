from django.utils.translation import gettext_lazy as _
from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from customers.models import Customer, Address, City, Country


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")


class CustomerRegisterSerializer(serializers.ModelSerializer):
    """
    email, password and password2 fields are required
    """

    password2 = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = Customer
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
        fields = ("first_name", "last_name", "email", "password", "password2")

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'password': 'Passwords must match'})

        return super().validate(attrs)

    def create(self, validated_data):
        user = Customer(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "country")


class AddressSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = ("id", "customer", "name", "full_name", "line_1", "line_2", "phone",
                  "district", "zipcode", "city", "is_default")

    def validate(self, attrs):
        validated_data = super().validate(attrs=attrs)
        instance = self.instance
        customer = validated_data.get("customer") or (self.instance and self.instance.customer)
        is_default = validated_data.get("is_default")
        with atomic():
            if is_default:
                if instance:
                    customer.addresses.exclude(id=instance.id).filter(is_default=True).update(is_default=False)
                else:
                    customer.addresses.filter(is_default=True).update(is_default=False)

        return validated_data

    def validate_full_name(self, value):
        if len(value) < 10:
            raise ValidationError(detail=_("Full name length must be bigger than 10"))
        return value


class AddressDetailedSerializer(AddressSerializer):
    customer = ProfileSerializer()
    city = CitySerializer()


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()
