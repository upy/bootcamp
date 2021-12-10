
from rest_framework import serializers

from payments.models import Bank, BankAccount


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ("name", )


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ("bank", "name", "iban")

class BankAccountDetailedSerializer(BankAccountSerializer):
    bank = BankSerializer()