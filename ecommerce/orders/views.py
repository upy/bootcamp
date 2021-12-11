from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from orders.filters import BillingAddressFilter, ShippingAddressFilter, \
    OrderFilter, OrderItemFilter, OrderBankAccountFilter
from orders.models import BillingAddress, Order, ShippingAddress, OrderItem, \
    OrderBankAccount
from orders.serializers import OrderSerializer, BillingAddressSerializer, \
    ShippingAddressSerializer, OrderDetailedSerializer, \
    BillingAddressDetailedSerializer, ShippingAddressDetailedSerializer, \
    OrderItemSerializer, OrderItemDetailedSerializer, \
    OrderBankAccountSerializer, OrderBankAccountDetailedSerializer


class BillingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    filterset_class = BillingAddressFilter
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detail": BillingAddressDetailedSerializer,
    }

class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    filterset_class = ShippingAddressFilter
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detail": ShippingAddressDetailedSerializer,
    }


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detail": OrderDetailedSerializer,
    }


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detail": OrderItemDetailedSerializer,
    }


class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    filterset_class = OrderBankAccountFilter
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detail": OrderBankAccountDetailedSerializer,
    }
