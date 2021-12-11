from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from payments.models import Bank, BankAccount


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Bank Name"))

    class Meta:
        model = Bank
        fields = ("name", )


class BankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Bank Name"))
    iban = filters.CharFilter(label=_("IBAN"))

    class Meta:
        model = BankAccount
        fields = ("name", )

