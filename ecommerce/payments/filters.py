from django_filters import rest_framework as filters
from payments.models import BankAccount


class BankAccountFilter(filters.FilterSet):

    class Meta:
        model = BankAccount
        fields = ("bank", "name", "iban")
