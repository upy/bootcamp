from django_filters import rest_framework as filters

from orders.models import (
    BillingAddress,
    Order,
    OrderBankAccount,
    OrderItem,
    ShippingAddress,
)


class OrderItemFilter(filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = ("order", "product")


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ("customer", "status")


class BillingAddressFilter(filters.FilterSet):
    class Meta:
        model = BillingAddress
        fields = ("full_name", "city")


class ShippingAddressFilter(filters.FilterSet):
    class Meta:
        model = ShippingAddress
        fields = ("full_name", "city")


class OrderBankAccountFilter(filters.FilterSet):
    class Meta:
        model = OrderBankAccount
        fields = ("name", "bank_name", "order")
