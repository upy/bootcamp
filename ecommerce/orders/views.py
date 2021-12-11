from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from orders.filters import OrderFilter
from orders.models import BillingAddress, ShippingAddress, Order, OrderItem, OrderBankAccount
from orders.serializers import BillingAddressSerializer, ShippingAddressSerializer, \
    OrderBankAccountSerializer, OrderSerializer, OrderItemSerializer, OrderItemDetailedSerializer



class BillingAddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

class OrderBankAccountViewSet(viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detailed": OrderItemDetailedSerializer,
    }
