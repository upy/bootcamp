from rest_framework import viewsets, permissions

from core.mixins import DetailedViewSetMixin
from orders.filters import OrderItemFilter, OrderFilter, BillingAddressFilter, ShippingAddressFilter, \
    OrderBankAccountFilter
from orders.models import OrderItem, Order, BillingAddress, ShippingAddress, OrderBankAccount
from orders.serializers import OrderItemSerializer, OrderSerializer, OrderItemDetailedSerializer, \
    OrderDetailedSerializer, BillingAddressSerializer, ShippingAddressSerializer, BillingAddressDetailedSerializer, \
    ShippingAddressDetailedSerializer, OrderBankAccountSerializer, OrderBankAccountDetailedSerializer


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detailed": OrderItemDetailedSerializer,
    }


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detailed": OrderDetailedSerializer,
    }


class BillingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    filterset_class = BillingAddressFilter
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detailed": BillingAddressDetailedSerializer,
    }


class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    filterset_class = ShippingAddressFilter
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detailed": ShippingAddressDetailedSerializer,
    }


class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    filterset_class = OrderBankAccountFilter
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detailed": OrderBankAccountDetailedSerializer,
    }
