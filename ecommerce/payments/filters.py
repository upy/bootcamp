from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from payments.models import Bank, BankAccount
from products.models import Product


class BankAccountFilter(filters.FilterSet):
    """
    Basket Filter
    """
    bank = filters.CharFilter(label=_("Bank"), method="filter_name")

    class Meta:
        model = BankAccount
        fields = ("bank", "name", "iban")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(bank__name__icontains=replaced_value) | Q(bank__name__icontains=value))
