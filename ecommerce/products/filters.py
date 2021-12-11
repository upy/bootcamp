from django.db.models import Q
from django.db.models.fields import related
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from products.models import Price, Product, Stock


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), method="filter_name")

    class Meta:
        model = Product
        fields = ("size", "color", "name")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(name__icontains=replaced_value) | Q(name__icontains=value))


class StockFilter(filters.FilterSet):

    class Meta:
        model = Stock
        fields = ("quantity", "product")


class PriceFilter(filters.FilterSet):

    class Meta:
        model = Price
        fields = ("amount", "product")