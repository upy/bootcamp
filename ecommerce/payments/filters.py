from django_filters import rest_framework as filters
from payments.models import Bank, BankAccount

class BankFilter(filters.FilterSet):

    class Meta:
        model = Bank
        fields = ("name")

class BankAccountFilter(filters.FilterSet):

    class Meta:
        model = BankAccount
        fields = ("bank", "name")
