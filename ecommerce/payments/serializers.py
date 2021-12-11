from rest_framework import serializers

from payments.models import Bank, BankAccount


class BankSerializer(serializers.ModelSerializer):
    """
    Bank Serializer
    """
    class Meta:
        model = Bank
        fields = ["name"]


class BankAccountSerializer(serializers.ModelSerializer):
    """
    Bank Account Serializer
    """
    class Meta:
        model = BankAccount
        fields = ["bank", "name", "iban"]


class BankAccountDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Bank Account Serializer
    """
    bank = BankSerializer

    class Meta:
        model = BankAccount
        fields = ["bank", "name", "iban"]
        
