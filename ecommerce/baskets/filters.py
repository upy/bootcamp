from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from baskets.models import Basket, BasketItem


class BasketFilter(filters.FilterSet):
    """
    Basket Models Filter
    """
    status = filters.CharFilter(label=_("Status"))

    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketItemFilter(filters.FilterSet):
    """
    BasketItem Models Filter
    """

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")
