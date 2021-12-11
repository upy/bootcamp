from django_filters import rest_framework as filters

from payments.models import BankAccount, Bank


class BankAccountFilter(filters.FilterSet):

    class Meta:
        model = BankAccount
        fields = ("bank", "name")


class BankFilter(filters.FilterSet):

    class Meta:
        model = Bank
        fields = ("name",)