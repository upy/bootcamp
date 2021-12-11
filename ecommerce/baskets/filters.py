from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from orders import enums
from baskets.models import Basket, BasketItem
from customers.filters import CustomerFilter
from products.filters import ProductFilter


class BasketFilter(filters.FilterSet):
    """
     Filter for BasketViewSet
    """
    customer = CustomerFilter
    status = filters.ChoiceFilter(label=_("Basket Status") ,choices=enums.OrderStatus.choices)

    class Meta:
        model = Basket
        fields = ("customer", "status")


class BasketItemFilter(filters.FilterSet):
    """
    Filter for BasketItemViewSet
    """
    price = filters.NumberFilter(label=_("Price"))
    product = ProductFilter
    basket = BasketFilter

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")
