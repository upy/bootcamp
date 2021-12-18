from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, \
    BasketDetailedSerializer,BasketPostSerializer
from core.mixins import DetailedViewSetMixin
from products.models import Product


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketPostSerializer,
        "add_to_basket": BasketPostSerializer,
        "remove_from_basket": BasketPostSerializer
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)

    @action(detail=True, methods=['post', 'put'])
    def add_to_basket(self, request, pk=None):
        """Add an item to a user's basket.
        Adding to basket is disallowed if there is not enough inventory for the
        product available. If there is, the quantity is increased on an existing
        basket item or a new basket item is created with that quantity and added
        to the basket.
        """
        basket = self.get_object()

        try:
            product = Product.objects.get(
                pk=request.data['items'][0]['product']
            )
            quantity = int(request.data['items'][0]['quantity'])
            price = request.data['items'][0]['price']
        except Exception as ex:
            print(ex)
            return Response('Required fields must be filled')
        """
        before adding the item to the basket, product's stock quantity is checked
        """

        if product.stock.quantity <= 0 or product.stock.quantity - quantity < 0:
            print("There is no more product available")
            return Response('There is no more product available')
        existing_basket_item = BasketItem.objects.filter(basket=basket, product=product).first()
        """
         before creating a new basket item check if it is in the basket already
         and if it is increase the quantity of that item
        """
        if existing_basket_item:
            existing_basket_item.quantity += quantity
            existing_basket_item.save()
        else:
            new_basket_item = BasketItem(basket=basket, product=product, quantity=quantity, price=price)
            new_basket_item.save()
        serializer = BasketPostSerializer(basket)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'put'])
    def remove_from_basket(self, request, pk=None):
        """Remove an item from a user's basket.
        Removing from the basket can be done with editing quantity for item.
        Edited quantity is decreased from the existing quantity.
        But after removing if items quantity is equal to zero item is deleted.
        """
        basket = self.get_object()
        try:
            product = Product.objects.get(
                pk=request.data['items'][0]['product']
            )
            quantity = int(request.data['items'][0]['quantity'])
            price = request.data['items'][0]['price']
        except Exception as ex:
            print(ex)
            return Response('Required fields must be filled')

        try:
            basket_item = BasketItem.objects.get(basket=basket, product=product)
        except Exception as ex:
            print(ex)
            return Response({'status': 'fail'})

        # if removing an item where the quantity of the item will become zero after process, remove the basket item
        # completely otherwise decrease the quantity of the basket item
        if basket_item.quantity - quantity <= 0:
            basket_item.delete()
        else:
            basket_item.quantity -= quantity
            basket_item.save()

        # return the updated basket to indicate success
        serializer = BasketPostSerializer(basket)
        return Response(serializer.data)
