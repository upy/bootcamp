from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import ugettext_lazy as _
from orders.models import BillingAddress, Order, OrderBankAccount, OrderItem, ShippingAddress

from payments.models import Bank, BankAccount


class BillingAddressFilter(filters.FilterSet):
    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")
    

class ShippingAddressFilter(filters.FilterSet):
    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")
    

class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class OrderBankAccountFilter(filters.FilterSet):
    name = filters.CharFilter(label=_('Name'), method='filter_name')

    class Meta:
        model = OrderBankAccount
        fields = ("name", "iban", "bank_name", "order")
    
    def filter_name(self, qs, name, value):
        return qs.filter(Q(name__icontains=value))


class OrderItemFilter(filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")