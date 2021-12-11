from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from products.models import Product, Category, Stock, Price


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), method="filter_name")

    class Meta:
        model = Product
        fields = ("size", "color", "name")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(name__icontains=replaced_value) | Q(name__icontains=value))


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Category"), lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ("name",)


# Stock Filter
class StockFilter(filters.FilterSet):
    quantity = filters.RangeFilter(label=_("Stock Quantity"))

    class Meta:
        model = Stock
        fields = ("product", "quantity")


# Price Filter
class PriceFilter(filters.FilterSet):
    amount = filters.NumberFilter(label=_("Price Amount"))

    class Meta:
        model = Price
        fields = ("product", "amount")
