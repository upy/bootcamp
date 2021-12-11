from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from customers.models import Address, Customer


class AddressFilter(filters.FilterSet):
    customer = filters.CharFilter(label=_("Customer"), method="filter_name")

    class Meta:
        model = Address
        fields = ("customer", "name", "full_name", "phone", "zipcode", "city",
                   "district")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(customer__first_name__icontains=replaced_value) | Q(customer__first_name__icontains=value))

class CustomerFilter(filters.FilterSet):
    """
    Customer Filter
    Filters customers by their names
    """
    first_name = filters.CharFilter(label=_("Name"), method="filter_name")

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email")

    def filter_name(self, qs, first_name, value):
            replaced_value = value.replace("Ş", "ş")
            return qs.filter(Q(first_name__icontains=replaced_value) | Q(first_name__icontains=value))
