from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from customers.models import Customer


class APITokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.is_superuser:
            raise AuthenticationFailed(_("Super user cannot login"))
        token = super().get_token(user)
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["email"] = user.email
        return token


class RegisterCustomerSerializer(serializers.ModelSerializer):

    password_1 = serializers.CharField(required=True, write_only=True, validators=[validate_password],
                                       style={"input_type": "password"})

    password_2 = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = Customer
        fields = ("email", "first_name", "last_name", "password_1", "password_2")

    def validate(self, attrs):
        if attrs["password_1"] != attrs["password_2"]:
            raise serializers.ValidationError({"password_1": "Passwords didn't match"})
        return attrs

    def create(self, validated_data):
        customer = Customer.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )

        customer.set_password(validated_data["password_1"])
        customer.save()

        return customer
