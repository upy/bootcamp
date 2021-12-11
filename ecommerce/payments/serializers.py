from django.db.transaction import atomic
from rest_framework import serializers

from payments.models import Bank, BankAccount


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = "__all__"


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        read_only_fields = ['id', 'created_at', 'updated_at']
        fields = "__all__"


class BankAccountDetailedSerializer(BankAccountSerializer):
    bank = BankSerializer()

    @atomic()
    def create(self, validated_data):
        bank = validated_data.pop("bank", None)
        bank_account = super().create(validated_data)
        if bank:
            serializer = BankSerializer(data=bank)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            bank_account.bank.add(*serializer.instance)
        return bank_account
