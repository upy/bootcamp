from rest_framework import viewsets

from orders.serializers import BillingAddressSerializer, ShippingAddressSerializer, \
    OrderSerializer, OrderBankAccountSerializer
from orders.models import BillingAddress, ShippingAddress, Order, OrderBankAccount


class BillingAddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderBankAccountViewSet(viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
