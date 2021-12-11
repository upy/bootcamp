from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem


class BillingAddressFilter(filters.FilterSet):
    ful_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    line1 = filters.CharFilter(label=_("Line1"), lookup_expr="icontains")
    line2 = filters.CharFilter(label=_("Line2"), lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    zipcode = filters.CharFilter(label=_("Zipcode"), lookup_expr="icontains")

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressFilter(filters.FilterSet):
    ful_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    line1 = filters.CharFilter(label=_("Line1"), lookup_expr="icontains")
    line2 = filters.CharFilter(label=_("Line2"), lookup_expr="icontains")
    phone = filters.CharFilter(label=_("Phone"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    zipcode = filters.CharFilter(label=_("Zipcode"), lookup_expr="icontains")

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderBankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")
    iban = filters.CharFilter(label=_("Iban"), lookup_expr="icontains")
    bank_name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")


class OrderFilter(filters.FilterSet):
    status = filters.CharFilter(label=_("Status"), lookup_expr="icontains")

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class OrderItemFilter(filters.FilterSet):
    product = filters.CharFilter(label=_("Product"), lookup_expr="icontains")

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")
