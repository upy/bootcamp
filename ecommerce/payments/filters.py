from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from payments.models import *


class BankFilter(filters.FilterSet):
    """
    Bank Filter
    """
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = Bank
        fields = ["name"]


class BankAccountFilter(filters.FilterSet):
    """
    Bank Account Filter
    """
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = BankAccount
        fields = ["bank", "name", "iban"]
