from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from products.models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), method="filter_name")

    class Meta:
        model = Product
        fields = ("size", "color", "name")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(
            Q(name__icontains=replaced_value) | Q(name__icontains=value))


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Category"), lookup_expr="icontains")


class StockFilter(filters.FilterSet):
    quantity = filters.RangeFilter(label=_("Quantity"))


class PriceFilter(filters.FilterSet):
    amount = filters.NumberFilter(label=_("Amount"))
