from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from baskets.models import Basket, BasketItem
from customers.filters import CustomerFilter
from products.filters import ProductFilter


class BasketFilter(filters.FilterSet):
    customer = CustomerFilter
    status = filters.CharFilter(label=_("Status"), field_name="status")

    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketItemFilter(filters.FilterSet):
    product = ProductFilter
    basket = BasketFilter
    price = filters.NumberFilter(label=_("Price"), lookup_expr="gte")

    class Meta:
        model = BasketItem
        fields = ("product", "basket", "price")
