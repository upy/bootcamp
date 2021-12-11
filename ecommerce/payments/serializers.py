from rest_framework import serializers

from payments.models import Bank, BankAccount


# Bank Serializer
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'name')


# Bank Account Serializer
class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('id', 'bank', 'name', 'iban')


# Bank Account Detailed Serializer - nested serializer
class BankAccountDetailedSerializer(BankAccountSerializer):
    banks = BankSerializer()
