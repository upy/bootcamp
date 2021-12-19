from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from baskets.enums import BasketStatus
from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, \
    BasketItemDetailedSerializer, BasketDetailedSerializer
from core.mixins import DetailedViewSetMixin


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = ()
    http_method_names = ["get",]

    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "list": BasketDetailedSerializer,
        "retrieve": BasketDetailedSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        if user_id:
            queryset = queryset.filter(customer_id=user_id, status=BasketStatus.OPEN)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user_id = request.user.id
        if not user_id:
            create_serializer = BasketSerializer(
                data={"customer": None, "status": BasketStatus.OPEN})
            create_serializer.is_valid(raise_exception=True)
            basket = create_serializer.save()
            serializer = self.get_serializer(basket)
            return Response(serializer.data, status=status.HTTP_200_OK)

        basket = queryset.first()
        if not basket:
            create_serializer = BasketSerializer(
                data={"customer": user_id, "status": BasketStatus.OPEN})
            create_serializer.is_valid(raise_exception=True)
            basket = create_serializer.save()
            serializer = self.get_serializer(basket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(basket)
            return Response(serializer.data, status=status.HTTP_200_OK)
