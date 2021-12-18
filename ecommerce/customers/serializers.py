from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from customers.models import Customer, Address, City, Country


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")


class CustomerRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="Email", write_only=True, required=True,
                                   validators=[EmailValidator, UniqueValidator(queryset=Customer.objects.all())])
    password = serializers.CharField(label=_("Password"), write_only=True, required=True,
                                     style={"input_type": "password"}, validators=[validate_password])
    password_confirm = serializers.CharField(label=_("Password Confirm"), write_only=True,
                                             required=True, style={"input_type": "password"})

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "password", "password_confirm")

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        new_customer = Customer.objects.create_user(**validated_data)
        return new_customer


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
