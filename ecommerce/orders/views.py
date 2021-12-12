from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from orders.models import  BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem
from orders.serializers import BillingAddressSerializer, ShippingAddressSerializer, OrderBankAccountSerializer, \
    OrderItemSerializer, OrderSerializer, \
    BillingAddressDetailedSerializer, ShippingAddressDetailedSerializer, OrderBankAccountDetailedSerializer, \
    OrderDetailedSerializer, OrderItemDetailedSerializer

class BillingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detailed": BillingAddressDetailedSerializer,
    }

class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detailed": ShippingAddressDetailedSerializer,
    }

class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detailed": OrderBankAccountDetailedSerializer,
    }

class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detailed": OrderDetailedSerializer,
    }

class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detailed": OrderItemDetailedSerializer,
    }

