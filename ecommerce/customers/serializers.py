from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.db.transaction import atomic
from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from customers.models import Customer, Address, City, Country
from ecommerce.settings import AUTH_PASSWORD_VALIDATORS


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email")


"""Create CustomerRegistrationSerializer"""
class CustomerRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label=_("Email"), write_only=True, required=True, validators=[
        EmailValidator, UniqueValidator(queryset=Customer.objects.all())])
    password = serializers.CharField(label=_("Password"), write_only=True, required=True, style={
        "input_type": "password"}, validators=[validate_password])
    password_repeat = serializers.CharField(label=_("Repeat Password"), write_only=True, 
        required=True, style={"input_type": "password"})
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "password", "password_repeat")

    def validate(self, data):
        """
        Check that the password is valid.
        """
        if data["password"] != data["password_repeat"]:
            raise ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop("password_repeat")
        new_customer = Customer.objects.create_user(**validated_data)
        return new_customer


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
