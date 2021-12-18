from rest_framework import viewsets
from rest_framework.response import Response

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, \
    BasketDetailedSerializer
from core.mixins import DetailedViewSetMixin
from rest_framework.decorators import action

from customers.models import Customer


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = ()
    http_method_names = ["get"]
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user.id
        return queryset.filter(basket__customer__id=user)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = ()
    http_method_names = ["get", "post", "options"]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "add_product": BasketItemSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user.id
        return queryset.filter(basket__customer__id=user)

    @action(detail=False, methods=["post", "options"])
    def add_product(self, request, pk=None, *args, **kwargs):
        """
        Create a new endpoint for adding product to basket item
        Check if Basket is exist otherwise create a new one
        :param request: request
        :param pk: None
        :param args:
        :param kwargs:
        :return: Dictionary
        """
        serializer = BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user.id
            customer_obj = Customer.objects.filter(id=user).first()
            product = serializer.validated_data.get("product")
            quantity = serializer.validated_data.get("quantity")
            price = serializer.validated_data.get("price")
            basket = Basket.objects.filter(customer=customer_obj, status="open").first()
            if not basket:
                basket = Basket.objects.create(customer=customer_obj, status="open")
            basket_item = BasketItem.objects.filter(basket__customer=user, product=product, price=float(str(price)))
            if not basket_item:
                basket_item = BasketItem.objects.create(basket=basket, product=product, quantity=quantity, price=float(str(price)))
            else:
                old_qty = basket_item[0].quantity
                new_qty = old_qty + float(quantity)
                basket_item[0].quantity = new_qty
                basket_item[0].save()
            serializer_detailed_data = BasketItemDetailedSerializer(basket_item[0]).data
            return Response(serializer_detailed_data)

