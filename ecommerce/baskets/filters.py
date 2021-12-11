from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from baskets.models import Basket, BasketItem
from products.models import Product


class BasketFilter(filters.FilterSet):
    """
    Basket Filter
    """
    customer = filters.CharFilter(label=_("Customer"), method="filter_name")

    class Meta:
        model = Basket
        fields = ("customer", "status")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(customer__first_name__icontains=replaced_value) | Q(customer__first_name__icontains=value))

class BasketItemFilter(filters.FilterSet):
    """
    Basket Item Filter
    """
    product = filters.CharFilter(label=_("Product-Name"), method="filter_name")

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(product__name__icontains=replaced_value) | Q(product__name__icontains=value))

