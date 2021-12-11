from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from baskets.models import Basket, BasketItem


class BasketFilter(filters.FilterSet):
    status = filters.CharFilter(label=_("Status"), method="filter_name")

    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketItemFilter(filters.FilterSet):

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "price")
