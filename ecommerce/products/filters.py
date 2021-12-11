from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from products.models import Product, Category, Stock, Price


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ("name",)


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), method="filter_name")

    class Meta:
        model = Product
        fields = ("size", "color", "name", "description", "color", "size", "categories")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(name__icontains=replaced_value) | Q(name__icontains=value))


class StockFilter(filters.FilterSet):
    class Meta:
        model = Stock
        fields = ("product", "quantity")


class PriceFilter(filters.FilterSet):
    class Meta:
        model = Price
        fields = ("product", "amount")
