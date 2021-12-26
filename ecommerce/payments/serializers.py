from rest_framework import serializers

from payments.models import Bank, BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ("id", "bank", "name", "iban")


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ("id", "name")


class BankAccountDetailedSerializer(BankAccountSerializer):
    bank = BankSerializer()
