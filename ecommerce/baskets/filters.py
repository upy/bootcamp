from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from baskets.models import Basket, BasketItem


class BasketFilter(filters.FilterSet):
    customer = filters.CharFilter(label=_("Customer"), method="filter_name")

    class Meta:
        model = Basket
        fields = ("customer", "status")

    def filter_name(self, name, qs, value):
        return qs.filter(Q(customer__first_name__icontains=replaced_value) | Q(customer__first_name__icontains=value))


class BasketItemFilter(filters.FilterSet):
    product = filters.CharFilter(label=_("Product"), method="filter_name")

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")

