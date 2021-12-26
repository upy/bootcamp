from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.mixins import DetailedViewSetMixin
from orders.filters import (
    OrderFilter
)
from orders.models import (
    Order
)
from orders.serializers import (
    CreateOrderSerializer,
    OrderDetailedSerializer,
    OrderSerializer
)


class OrderViewSet(
    DetailedViewSetMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    serializer_action_classes = {
        "detailed_list": OrderDetailedSerializer,
        "detailed": OrderDetailedSerializer,
        "create": CreateOrderSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        return queryset.filter(customer_id=user_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        order_serializer = OrderDetailedSerializer(instance=serializer.instance)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
