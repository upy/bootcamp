from django_filters import rest_framework as filters

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem

class BillingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")

    class Meta:
        model = BillingAddress
        fields = ("full_name", "phone", "district", "zipcode", "city")


class ShippingAddressFilter(filters.FilterSet):
    full_name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "phone", "district", "zipcode", "city")


class OrderBankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ("name", "bank_name", "order")

class OrderFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields = ("customer", "status", "billing_address", "shipping_address")

class OrderItemFilter(filters.FilterSet):

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")




