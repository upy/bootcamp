from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from customers.models import Customer


class CustomerFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("First Name"), method="filter_name")

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(first_name__icontains=replaced_value) | Q(first_name__icontains=value))
