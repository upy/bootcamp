from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from baskets.filters import BasketItemFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketItemDetailedSerializer
from core.mixins import DetailedViewSetMixin
from products.models import Product


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
        # import pdb; pdb.set_trace()
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

    @action(detail=False, methods=["post"], http_method_names=["post"])
    def add_to_cart(self, request, pk=None):
        user_id = self.request.user.id
        product = Product.objects.get(id=request.data["product"])
        quantity = request.data["quantity"]
        price = product.price
        basket = Basket.objects.filter(customer__id=user_id, status="open").first()
        if not basket:
            basket = Basket.objects.create(customer_id=user_id, status="open")
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
