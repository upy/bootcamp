from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
# from orders.filters import ProductFilter
from orders.models import Order
from orders.serializers import *


class OrderViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detailed": OrderDetailedSerializer,
    }


class BillingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    # filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": BillingAddressDetailedSerializer,
        "detailed": BillingAddressDetailedSerializer,
    }


class ShippingAddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    # filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": ShippingAddressDetailedSerializer,
        "detailed": ShippingAddressDetailedSerializer,
    }


class OrderBankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderBankAccount.objects.all()
    serializer_class = OrderBankAccountSerializer
    # filterset_class = ProductFilter
    serializer_action_classes = {
        "detailed_list": OrderBankAccountDetailedSerializer,
        "detailed": OrderBankAccountDetailedSerializer,
    }
