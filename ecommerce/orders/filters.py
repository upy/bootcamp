
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class OrderFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), method="")

    class Meta:
        model = Order
        fields = ("customer", "status")