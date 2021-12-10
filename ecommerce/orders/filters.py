from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from orders.models import Order, OrderItem, BillingAddress, ShippingAddress, OrderBankAccount


class BillingAddressFilter(filters.FilterSet):

    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    line_1 = filters.CharFilter(label=_("Address Line 1"), lookup_expr="icontains")
    line_2 = filters.CharFilter(label=_("Address Line 2"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    city = filters.CharFilter(label=_("City"), lookup_expr="icontains")

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2",
                  "phone", "district", "zipcode", "city")


class ShippingAddressFilter(filters.FilterSet):

    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    line_1 = filters.CharFilter(label=_("Address Line 1"), lookup_expr="icontains")
    line_2 = filters.CharFilter(label=_("Address Line 2"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    city = filters.CharFilter(label=_("City"), lookup_expr="icontains")

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2",
                  "phone", "district", "zipcode", "city")


class OrderBankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")
    bank_name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")


class OrderFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "total_price" )


class OrderItemFilter(filters.FilterSet):

    product = filters.CharFilter(label=_("Product Name"), lookup_expr="icontains" )

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")
