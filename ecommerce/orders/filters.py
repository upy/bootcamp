from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from orders import enums
from orders.models import OrderItem, Order, OrderBankAccount, ShippingAddress, BillingAddress

from customers.filters import CityFilter,  CustomerFilter
from baskets.filters import BasketFilter


class BillingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"))
    city = CityFilter

    class Meta:
        model = BillingAddress
        fields = ("full_name", "city")


class ShippingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"))
    city = CityFilter

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "city")


class OrderFilter(filters.FilterSet):
    customer = CustomerFilter
    basket = BasketFilter
    status = filters.ChoiceFilter(choices=enums.OrderStatus.choices)

    class Meta:
        model = Order
        fields = ("customer", "basket", "status")


class OrderItemFilter(filters.FilterSet):
    order = OrderFilter
    product = filters.CharFilter(label=_("Product"))

    class Meta:
        model = OrderItem
        fields = ("order", "product")


class OrderBankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"))
    iban = filters.CharFilter(label=_("IBAN"))
    bank_name = filters.CharFilter(label=_("Bank Name"))
    order = OrderFilter

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")




