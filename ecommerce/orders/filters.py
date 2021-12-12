from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from baskets.filters import BasketFilter
from customers.filters import CityFilter, CustomerFilter
from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem
from products.filters import ProductFilter


class BillingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Billing Address"), lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"), lookup_expr="iexact")
    city = CityFilter

    class Meta:
        model = BillingAddress
        fields = ("full_name", "phone", "city",)


class ShippingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Shipping Address"), lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"), lookup_expr="iexact")
    city = CityFilter

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "phone", "city",)


class OrderFilter(filters.FilterSet):
    customer = CustomerFilter
    basket = BasketFilter
    status = filters.CharFilter(label=_("Status"), lookup_expr="iexact")

    class Meta:
        model = Order
        fields = ("customer", "basket", "status",)


class OrderBankAccountFilter(filters.FilterSet):
    order = OrderFilter
    name = filters.CharFilter(label=_("City Name"), lookup_expr="icontains")
    iban = filters.CharFilter(label=_("IBAN"), lookup_expr="iexact")
    bank_name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")


class OrderItemFilter(filters.FilterSet):
    order = OrderFilter
    product = ProductFilter

    class Meta:
        model = OrderItem
        fields = ("order", "product",)