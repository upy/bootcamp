from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from customers.filters import CityFilter
from orders.models import BillingAddress, ShippingAddress, Order, OrderItem, \
    OrderBankAccount


# Billing Address Filter
class BillingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"),
                                   lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"))
    line_1 = filters.CharFilter(label=_("Line 1"), lookup_expr="icontains")
    line_2 = filters.CharFilter(label=_("Line 2"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    zipcode = filters.CharFilter(label=_("Zipcode"))
    city = CityFilter

    class Meta:
        model = BillingAddress
        fields = (
            "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


# Shipping Address Filter
class ShippingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"),
                                   lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"))
    line_1 = filters.CharFilter(label=_("Line 1"), lookup_expr="icontains")
    line_2 = filters.CharFilter(label=_("Line 2"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    zipcode = filters.CharFilter(label=_("Zipcode"))
    city = CityFilter

    class Meta:
        model = ShippingAddress
        fields = (
            "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


# Order Filter
class OrderFilter(filters.FilterSet):
    total_price = filters.NumberFilter(label=_("Total Price"))

    class Meta:
        model = Order
        fields = (
            "customer", "basket", "status", "billing_address", "shipping_address",
            "total_price")


# Order Item Filter
class OrderItemFilter(filters.FilterSet):
    product = filters.CharFilter(label=_("Product"), lookup_expr="icontains")
    price = filters.NumberFilter()

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")


# Order Bank Account Filter
class OrderBankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Order Bank Account Name"),
                              lookup_expr="icontains")
    iban = filters.CharFilter(label=_("IBAN"), lookup_expr="exact")
    bank_name = filters.CharFilter(label=_("Bank Name"),
                                   lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")
