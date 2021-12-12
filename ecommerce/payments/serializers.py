from core.models import get_all_base_abstract_model_attrs
from payments.models import *
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = get_all_bank_attrs() + get_all_base_abstract_model_attrs() + "id"


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = get_all_bank_account_attrs() + get_all_base_abstract_model_attrs() + "id"


class BankDetailedSerializer(serializers.ModelSerializer):
    bank_accounts = BankAccountSerializer(many=True)
    class Meta:
        model = Bank
        fields = get_all_bank_attrs() + get_all_base_abstract_model_attrs() + "id"


class BankAccountDetailedSerializer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        model = BankAccount
        fields = get_all_bank_account_attrs() + get_all_base_abstract_model_attrs() + "id"
