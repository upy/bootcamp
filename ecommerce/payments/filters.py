from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from payments.models import Bank, BankAccount


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = Bank
        fields = ("name",)


class BankAccountFilter(filters.FilterSet):
    bank = BankFilter
    name = filters.CharFilter(label=_("Bank Account Name"), lookup_expr="icontains")
    iban = filters.CharFilter(label=_("Phone"), lookup_expr="iexact")

    class Meta:
        model = BankAccount
        fields = ("bank", "name", "iban",)
