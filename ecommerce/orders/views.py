from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from orders.filter import ShippingAddressFilter, BillingAddressFilter, OrderBankAccountFilter, OrderFilter, \
    OrderItemFilter
from orders.models import ShippingAddress, BillingAddress, OrderBankAccount, Order, OrderItem
from orders.serializers import ShippingAddressSerializer, BillingAddressSerializer, OrderBankAccountSerializer, \
    OrderSerializer, \
    OrderItemSerializer, ShippingAddressDetailedSerializer, BillingAddressDetailedSerializer, OrderDetailedSerializer, \
    OrderBankAccountDetailedSerializer, OrderItemDetailedSerializer


class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    filterset_class = ShippingAddressFilter
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detailed": ShippingAddressDetailedSerializer,
    }


class BillingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    filterset_class = BillingAddressFilter
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detailed": BillingAddressDetailedSerializer,
    }


class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    filterset_class = OrderBankAccountFilter
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detailed": OrderBankAccountDetailedSerializer,
    }


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detailed": OrderDetailedSerializer,
    }


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detailed": OrderItemDetailedSerializer,
    }
