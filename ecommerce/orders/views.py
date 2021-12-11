from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from orders.filters import BillingAddressFilter, OrderBankAccountFilter, OrderFilter, \
    OrderItemFilter, ShippingAddressFilter
from orders.serializers import BillingAddressSerializer, OrderBankAccountSerializer, \
    OrderItemSerializer, OrderSerializer, ShippingAddressSerializer
from orders.models import BillingAddress, Order, OrderBankAccount, OrderItem, ShippingAddress


class BillingAddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    filterset_class = BillingAddressFilter
    # serializer_action_classes = {
    #     "detailed_list": BillingAddressDetailedSerializer,
    #     "detailed": BillingAddressDetailedSerializer
    # }



class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    filterset_class = ShippingAddressFilter
    # serializer_action_classes = {
    #     "detailed_list": ShippingAddressDetailedSerializer,
    #     "detailed": ShippingAddressDetailedSerializer
    # }


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    # serializer_action_classes = {
    #     "detailed_list": OrderDetailedSerializer,
    #     "detailed": OrderDetailedSerializer
    # }


class OrderBankAccountViewSet(viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    filterset_class = OrderBankAccountFilter
    # serializer_action_classes = {
    #     "detailed_list": OrderBankAccountDetailedSerializer,
    #     "detailed": OrderBankAccountDetailedSerializer
    # }


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter
    # serializer_action_classes = {
    #     "detailed_list": OrderItemDetailedSerializer,
    #     "detailed": OrderItemDetailedSerializer
    # }