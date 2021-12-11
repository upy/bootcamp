from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from payments.models import Bank, BankAccount


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = Bank
        fields = ("name", )


class BankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")
    iban = filters.CharFilter(label=_("Iban"), lookup_expr="icontains")

    class Meta:
        model = BankAccount
        fields = ("bank", "name", "iban")
