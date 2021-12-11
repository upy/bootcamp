from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from orders.models import Order, OrderItem



class OrderFilter(filters.FilterSet):
    """
    Order Filter
    """
    customer = filters.CharFilter(label=_("Customer"), method="filter_name")

    class Meta:
        model = Order
        fields = ("customer", "basket", "status")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(customer__first_name__icontains=replaced_value) | Q(customer__first_name__icontains=value))
