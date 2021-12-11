from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from baskets.models import Basket, BasketItem


class BasketFilter(filters.FilterSet):
    customer = filters.CharFilter(label=_("Customer"), method="filter_name")

    class Meta:
        model = Basket
        fields = ("customer", "status")

    @staticmethod
    def filter_name(self, qs, name, value):
        return qs.filter(customer__first_name__icontains=value)


class BasketItemFilter(filters.FilterSet):
    product = filters.CharFilter(label=_("Product"), method="filter_name")

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")

