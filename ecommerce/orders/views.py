from rest_framework import viewsets
from core.mixins import DetailedViewSetMixin
from orders.filters import OrderFilter
from orders.models import Order, OrderItem, OrderBankAccount, ShippingAddress, BillingAddress
from orders.serializer import OrderSerializer, OrderItemSerializer, OrderBankAccountSerializer, BillingAddressSerializer, ShippingAddressSerializer, \
            OrderDetailedSerializer


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    filterset_class = OrderFilter
    serializer_class = OrderSerializer

class OrderBankAccountViewSet(viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

class BillingAddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer

class OrderDetailedViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailedSerializer
    http_method_names = ["get"]