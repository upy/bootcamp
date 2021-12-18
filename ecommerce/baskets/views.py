from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from baskets.filters import BasketItemFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketItemDetailedSerializer
from core.mixins import DetailedViewSetMixin



class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ["get"]
    permission_classes = ()
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        return queryset.filter(basket__customer__id=user_id)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "delete"]
    permission_classes = ()
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemDetailedSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "add_to_cart": BasketItemSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        return queryset.filter(basket__customer__id=user_id)

    @action(detail=False, methods=["get", "post", "delete"], http_method_names=["get", "post", "delete"])
    def add_to_cart(self, request):
        if self.request.method == 'GET':
            data = [
                BasketItemDetailedSerializer(model).data
                for model in self.get_queryset()
            ]
            return Response(data, status=status.HTTP_200_OK)
        elif self.request.method == 'POST':
            serializer = BasketItemSerializer(data=self.request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            user_id = self.request.user.id
            product = serializer.validated_data.get("product")
            quantity = serializer.validated_data.get("quantity")
            price = product.price
            basket = Basket.objects.filter(customer__id=user_id, status="open").first()
            if not basket:
                basket = Basket.objects.create(customer__id=user_id, status="open")
            basket_item = BasketItem.objects.filter(
                basket__customer__id=user_id, product=product, price=float(str(price))).first()
            if not basket_item:
                basket_item = BasketItem.objects.create(
                    basket=basket, product=product, quantity=quantity, price=float(str(price))
                )
            else:
                basket_item.quantity += float(quantity)
                basket_item.save()
            serializer_detailed_data = BasketItemDetailedSerializer(basket_item).data
            return Response(dict(serializer_detailed_data))
        elif self.request.method == 'DELETE':
            user_id = self.request.user.id
            basket = Basket.objects.filter(customer__id=user_id, status="open").first()
            if not basket:
                return Response(status=status.HTTP_404_NOT_FOUND)
            basket_item = BasketItem.objects.filter(basket__customer__id=user_id).first()
            basket_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            