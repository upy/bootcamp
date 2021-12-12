from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")


class BankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=("Bank Name"), lookup_expr="icontains")
    iban = filters.CharFilter(label=("IBAN"), lookup_expr="exact")


