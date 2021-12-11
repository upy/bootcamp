from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from baskets.models import Basket


class BasketFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), method="")

    class Meta:
        model = Basket
        fields = ("customer", )
