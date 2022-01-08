from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from payments.models import Bank, BankAccount


class BankFilter(filters.FilterSet):

    class Meta:
        model = Bank
        fields = ("name", )


class BankAccountFilter(filters.FilterSet):

    class Meta:
        model = BankAccount
        fields = ("name", )

