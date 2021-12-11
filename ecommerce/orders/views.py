from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
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
#     filterset_class = BillingAddressFilter
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detail": BillingAddressDetailedSerializer,
    }

class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detail": ShippingAddressDetailedSerializer,
    }


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detail": OrderDetailedSerializer,
    }


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detail": OrderItemDetailedSerializer,
    }


class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detail": OrderBankAccountDetailedSerializer,
    }
