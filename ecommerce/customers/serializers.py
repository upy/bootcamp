from django.contrib.auth.password_validation import validate_password
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from customers.models import Address, City, Country, Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class CustomerCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        label=_("Password repeat"),
        max_length=128,
        write_only=True,
        style={"input_type": "password"},
    )
    password = serializers.CharField(
        label=_("Password"),
        max_length=128,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "password", "password2")
        extra_kwargs = {
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs["password"]
        password2 = attrs["password2"]
        if password != password2:
            raise ValidationError(
                detail={"password2": _("Your passwords must be same")}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2", None)
        instance = Customer.objects.create_user(**validated_data)
        return instance


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
        fields = (
            "id",
            "customer",
            "name",
            "full_name",
            "line_1",
            "line_2",
            "phone",
            "district",
            "zipcode",
            "city",
            "is_default",
        )

    def validate(self, attrs):
        validated_data = super().validate(attrs=attrs)
        instance = self.instance
        customer = validated_data.get("customer") or (
            self.instance and self.instance.customer
        )
        is_default = validated_data.get("is_default")
        with atomic():
            if is_default:
                if instance:
                    customer.addresses.exclude(id=instance.id).filter(
                        is_default=True
                    ).update(is_default=False)
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
