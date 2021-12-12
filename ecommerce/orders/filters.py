from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _


from customers.filters import CityFilter, CustomerFilter
from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem
from products.filters import ProductFilter
from baskets.filters import BasketFilter


class BillingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    city = CityFilter

    class Meta:
        model = BillingAddress
        fields = ("full_name", "city")


class ShippingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    city = CityFilter

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "city")


class OrderFilter(filters.FilterSet):
    customer = CustomerFilter
    basket = BasketFilter

    class Meta:
        model = Order
        fields = ("customer", "basket", )


class OrderBankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"),lookup_expr="icontains")
    iban = filters.CharFilter(label=_("IBAN"), lookup_expr="icontains")
    bank_name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")


class OrderItemFilter(filters.FilterSet):
    product = ProductFilter
    order = OrderFilter

    class Meta:
        model = OrderItem
        fields = ("order", "product")
