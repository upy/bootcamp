from django.db.transaction import atomic
from rest_framework import serializers

from payments.models import Bank, BankAccount


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ("id", "name",)


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ("id", "bank", "name", "iban",)


class BankAccountDetailedSerializer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        model = BankAccount
        fields = ("id", "bank", "name", "iban",)

    @atomic()
    def create(self, validated_data):
        bank = validated_data.pop("bank", None)
        bank_account = super().create(validated_data)
        if bank:
            serializer = BankSerializer(data=bank, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            bank_account.bank.add(*serializer.instance)
        return bank_account
