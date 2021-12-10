from django_filters import rest_framework as filters

from baskets.models import Basket, BasketItem
from customers.filters import CustomerFilter
from products.filters import ProductFilter


class BasketFilter(filters.FilterSet):
    customer = CustomerFilter

    class Meta:
        model = Basket
        fields = ("customer",)


class BasketItemFilter(filters.FilterSet):
    product = ProductFilter
    basket = BasketFilter

    class Meta:
        model = BasketItem
        fields = ("basket", "product")
