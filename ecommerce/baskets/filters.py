from django_filters import rest_framework as filters

from baskets.models import Basket, BasketItem


class Basket(filters.FilterSet):
    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketItem(filters.FilterSet):
    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")
