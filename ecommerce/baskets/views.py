from django.db.transaction import atomic
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from baskets.enums import BasketStatus
from baskets.filters import BasketFilter
from baskets.models import Basket
from baskets.serializers import (
    BasketDetailedSerializer,
    BasketItemSerializer,
    BasketItemValidateSerializer,
    BasketSerializer,
)
from core.mixins import DetailedViewSetMixin


class BasketViewSet(
    DetailedViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = ()
    lookup_field = "slug"
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "list": BasketDetailedSerializer,
        "retrieve": BasketDetailedSerializer,
        "basket_item": BasketItemValidateSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        if user_id:
            loggined_basket = queryset.filter(
                customer_id=user_id, status=BasketStatus.OPEN
            ).first()
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            if lookup_url_kwarg in self.kwargs:
                filter_kwargs = {
                    self.lookup_field: self.kwargs[lookup_url_kwarg]
                }  # {"slug": "5667880-23423sdfsd"}
                anonymous_basket = (
                    queryset.filter(**filter_kwargs)
                    .filter(customer__isnull=True)
                    .first()
                )
                if loggined_basket and anonymous_basket:
                    with atomic():
                        loggined_basket.status = BasketStatus.MERGED
                        loggined_basket.save(update_fields=["status"])
                        anonymous_basket.customer_id = user_id
                        anonymous_basket.save(update_fields=["customer_id"])
                        for old_basket_item in loggined_basket.basketitem_set.all():
                            new_basket_item = anonymous_basket.basketitem_set.filter(
                                product_id=old_basket_item.product_id
                            ).first()
                            quantity = old_basket_item.quantity
                            if new_basket_item:
                                quantity += new_basket_item.quantity
                            item_serializer = BasketItemSerializer(
                                instance=new_basket_item,
                                data={
                                    "basket": anonymous_basket.id,
                                    "product": old_basket_item.product_id,
                                    "quantity": quantity,
                                    "price": old_basket_item.product.price.amount,
                                },
                            )
                            if item_serializer.is_valid():
                                item_serializer.save()
            queryset = queryset.filter(customer_id=user_id, status=BasketStatus.OPEN)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user_id = request.user.id
        if not user_id:
            create_serializer = BasketSerializer(
                data={"customer": None, "status": BasketStatus.OPEN}
            )
            create_serializer.is_valid(raise_exception=True)
            basket = create_serializer.save()
            serializer = self.get_serializer(basket)
            return Response(serializer.data, status=status.HTTP_200_OK)

        basket = queryset.first()
        if not basket:
            create_serializer = BasketSerializer(
                data={"customer": user_id, "status": BasketStatus.OPEN}
            )
            create_serializer.is_valid(raise_exception=True)
            basket = create_serializer.save()
            serializer = self.get_serializer(basket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(basket)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True)
    def add_basket_item(self, *args, **kwargs):
        basket = self.get_object()
        add_basket_item_serializer = BasketItemValidateSerializer(
            data=self.request.data
        )
        add_basket_item_serializer.is_valid(raise_exception=True)

        product = add_basket_item_serializer.validated_data["product"]
        quantity = add_basket_item_serializer.validated_data["quantity"]
        basket_item = basket.basketitem_set.filter(product_id=product.id).first()
        if quantity > 0:
            if basket_item:
                quantity = quantity + basket_item.quantity
            item_serializer = BasketItemSerializer(
                instance=basket_item,
                data={
                    "basket": basket.id,
                    "product": product.id,
                    "quantity": quantity,
                    "price": product.price.amount,
                },
            )
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()

        serializer = BasketDetailedSerializer(instance=basket)
        return Response(serializer.data)

    @action(methods=["patch"], detail=True)
    def basket_item(self, *args, **kwargs):
        basket = self.get_object()
        add_basket_item_serializer = BasketItemValidateSerializer(
            data=self.request.data
        )
        add_basket_item_serializer.is_valid(raise_exception=True)

        product = add_basket_item_serializer.validated_data["product"]
        quantity = add_basket_item_serializer.validated_data["quantity"]

        basket_item = basket.basketitem_set.filter(product_id=product.id).first()
        if quantity > 0:
            item_serializer = BasketItemSerializer(
                instance=basket_item,
                data={
                    "basket": basket.id,
                    "product": product.id,
                    "quantity": quantity,
                    "price": product.price.amount,
                },
            )
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()
        elif basket_item:
            basket_item.delete()

        serializer = BasketDetailedSerializer(instance=basket)
        return Response(serializer.data)
