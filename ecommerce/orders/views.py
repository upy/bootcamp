from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer, OrderItemDetailedSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    serializer_action_classes = {
        "detailed_list": OrderItemDetailedSerializer,
        "detailed": OrderItemDetailedSerializer,
    }
