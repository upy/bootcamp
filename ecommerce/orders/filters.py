from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from orders import enums
from orders.models import OrderItem, Order, OrderBankAccount, ShippingAddress, BillingAddress

from customers.filters import CityFilter,  CustomerFilter
from baskets.filters import BasketFilter


class BillingAddressFilter(filters.FilterSet):

    class Meta:
        model = BillingAddress
        fields = ("full_name", "city")


class ShippingAddressFilter(filters.FilterSet):

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "city")


class OrderFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields = ("customer", "basket", "status")


class OrderItemFilter(filters.FilterSet):

    class Meta:
        model = OrderItem
        fields = ("order", "product")


class OrderBankAccountFilter(filters.FilterSet):

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")




