
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from payments.models import BankAccount


class BankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), method="")

    class Meta:
        model = BankAccount
        fields = ("bank",)