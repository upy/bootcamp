from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from customers.filters import CustomerFilter, CityFilter
from baskets.filters import BasketFilter
from products.filters import ProductFilter
from orders.models import Order, OrderBankAccount, OrderItem, BillingAddress, ShippingAddress


class OrderFilter(filters.FilterSet):
    customer = CustomerFilter
    basket = BasketFilter
    status = filters.CharFilter(label=_("Status"), lookup_expr="iexact")

    class Meta:
        model = Order
        fields = ("customer", "basket", "status",)


class OrderItemFilter(filters.FilterSet):
    order = OrderFilter
    product = ProductFilter

    class Meta:
        model = OrderItem
        fields = ("order", "product",)


class OrderBankAccountFilter(filters.FilterSet):
    order = OrderFilter
    name = filters.CharFilter(label=_("City Name"), lookup_expr="icontains")
    iban = filters.CharFilter(label=_("IBAN"), lookup_expr="iexact")
    bank_name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")


class BillingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"),
                                   lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"))
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    zipcode = filters.CharFilter(label=_("Zipcode"))
    city = CityFilter

    class Meta:
        model = BillingAddress
        fields = (
            "full_name", "phone", "district", "zipcode", "city")


class ShippingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"),
                                   lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"))
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    zipcode = filters.CharFilter(label=_("Zipcode"))
    city = CityFilter

    class Meta:
        model = ShippingAddress
        fields = (
            "full_name", "phone", "district", "zipcode", "city")
