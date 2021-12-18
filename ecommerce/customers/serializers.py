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


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, required=True, validators=[EmailValidator(),
                                                              UniqueValidator(queryset=Customer.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = fields = ("id", "email", "password", "password_repeat", "first_name", "last_name")

    def validate(self, attrs):
        if attrs["password"] != attrs["password_repeat"]:
            raise ValidationError(_("Passwords are not same"))
        return attrs

    def create(self, validated_data):
        customer = Customer.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return customer


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
