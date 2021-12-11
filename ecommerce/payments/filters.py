from django_filters import rest_framework as filters

from customers.models import City, Country, Customer, get_all_customer_attrs, Address, get_all_address_attrs
from orders.models import BillingAddress, get_all_billing_address_attrs, ShippingAddress, \
    get_all_shipping_address_attrs, get_all_order_bank_account_attrs, OrderBankAccount, Order, get_all_order_attrs, \
    OrderItem, get_all_order_item_attrs


class BillingAddressFilter(filters.FilterSet):
    class Meta:
        model = BillingAddress
        fields = get_all_billing_address_attrs()


class ShippingAddressFilter(filters.FilterSet):
    class Meta:
        model = ShippingAddress
        fields = get_all_shipping_address_attrs()


class OrderBankAccountFilter(filters.FilterSet):
    class Meta:
        model = OrderBankAccount
        fields = get_all_order_bank_account_attrs()


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = get_all_order_attrs()


class OrderItem(filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = get_all_order_item_attrs()
