from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, \
    BasketDetailedSerializer
from core.mixins import DetailedViewSetMixin


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
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
        user = self.request.user
        if user.is_staff:  # to enable admin to see all baskets items.
            return queryset
        return queryset.filter(basket__customer=user)


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
        "add_to_basket": BasketSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_staff:  # to enable admin to see all baskets.
            return queryset

        return queryset.filter(customer=user)

    @action(detail=False, methods=['post'])
    def add_to_basket(self, request):
        serializer = BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    @action(detail=False, methods=['post', 'get'], http_method_names = ['get', 'post'])
    def add_basket_item(self, request):
        
        if self.request.method == 'GET':
            return self.list(request)
        elif self.request.method == 'POST':
            serializer = BasketItemSerializer(data=request.data)
            if serializer.is_valid():
                user_id = self.request.user.id
                product = serializer.validated_data.get("product")
                quantity = serializer.validated_data.get("quantity")
                price = serializer.validated_data.get("price")
                basket = Basket.objects.filter(customer__id=user_id, status="open").first()

                if not basket:
                    basket = Basket.objects.create(customer__id=user_id, status="open")

                basket_item = BasketItem.objects.filter(basket__customer__id=user__id, product=product,
                                                        price=float(str(price))).first()
                if not basket_item:
                    basket_item = BasketItem.objects.create(
                        basket=basket, product=product, quantity=quantity, price=float(str(price))
                    )
                else:
                    basket_item.quantity += float(quantity)
                    basket.item.save()
                serializer_detailed_data = BasketItemDetailedSerializer(basket_item).data
                return Response(dict(serializer_detailed_data))


"""
