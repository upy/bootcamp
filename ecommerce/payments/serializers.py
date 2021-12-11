from rest_framework import serializers

from payments.models import BankAccount, Bank


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ("id", "name")


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ("id", "bank", "name", "iban")


class BankAccountDetailedSerializer(BankAccountSerializer):
    bank = BankSerializer()
