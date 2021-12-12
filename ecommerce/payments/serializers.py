from rest_framework import serializers
from payments.models import Bank, BankAccount
from django.db.transaction import atomic


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ("id", "name",)


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ("id", "bank", "name", "iban",)


class BankAccountDetailedSerializer(BankAccountSerializer):
    bank = BankSerializer()

    @atomic()
    def create(self, validated_data):
        bank = validated_data.pop("bank", None)
        bank_acc = super().create(validated_data)
        if bank:
            serializer = BankSerializer(data=bank)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            bank_acc.bank.add(*serializer.instance)
        return bank_acc