from rest_framework import viewsets

from baskets.models import Basket
from baskets.serializer import BasketSerializer


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
