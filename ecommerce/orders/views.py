from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from orders.filters import OrderItemFilter, OrderFilter, BillingAddressFilter, ShippingAddressFilter, \
    OrderBankAccountFilter
from orders.models import OrderItem, Order, BillingAddress, ShippingAddress, OrderBankAccount
from orders.serializers import OrderItemSerializer, OrderSerializer, OrderItemDetailedSerializer, \
    OrderDetailedSerializer, BillingAddressSerializer, ShippingAddressSerializer, BillingAddressDetailedSerializer, \
    ShippingAddressDetailedSerializer, OrderBankAccountSerializer, OrderBankAccountDetailedSerializer


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detailed": OrderItemDetailedSerializer,
    }


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detailed": OrderDetailedSerializer,
    }

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {"customer": self.request.user}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)


class BillingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    filterset_class = BillingAddressFilter
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detailed": BillingAddressDetailedSerializer,
    }


class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    filterset_class = ShippingAddressFilter
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detailed": ShippingAddressDetailedSerializer,
    }


class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    filterset_class = OrderBankAccountFilter
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detailed": OrderBankAccountDetailedSerializer,
    }
