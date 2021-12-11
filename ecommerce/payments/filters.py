from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from payments.models import Bank, BankAccount


# Bank Filter
class BankFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = Bank
        fields = ("name",)


# Bank Account Filter
class BankAccountFilter(filters.FilterSet):
    bank = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")
    name = filters.CharFilter(label=_("Bank Account Name"), lookup_expr="icontains")

    class Meta:
        model = BankAccount
        fields = ("bank", "name", "iban")
