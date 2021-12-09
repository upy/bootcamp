from rest_framework import viewsets
from core.mixins import DetailedViewSetMixin
from orders.models import Order, OrderBankAccount, OrderItem, \
    BillingAddress, ShippingAddress
from orders.serializers import BillingAddressSerializer, BillingAddressDetailedSerializer, \
    ShippingAddressSerializer, ShippingAddressDetailedSerializer, OrderSerializer, \
    OrderDetailedSerializer, OrderBankAccountSerializer, OrderBankAccountDetailedSerializer,\
    OrderItemSerializer, OrderItemDetailedSerializer
from orders.managers import BillingAddressQuerySet


class BillingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BillingAddress.objects.action_detailed_list()
    serializer_class = BillingAddressSerializer
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detailed": BillingAddressDetailedSerializer,
    }


class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.action_detailed_list()
    serializer_class = ShippingAddressSerializer
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detailed": ShippingAddressDetailedSerializer,
    }


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.action_detailed_list()
    serializer_class = OrderSerializer
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detailed": OrderDetailedSerializer,
    }


class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.action_detailed_list()
    serializer_class = OrderBankAccountSerializer
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detailed": OrderBankAccountDetailedSerializer,
    }


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.action_detailed_list()
    serializer_class = OrderItemSerializer
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detailed": OrderItemDetailedSerializer,
    }
