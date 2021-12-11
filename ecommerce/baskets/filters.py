from django_filters import rest_framework as filters

from baskets.models import Basket, BasketItem

#Basket Filter
class BasketFilter(filters.FilterSet):
    class Meta:
        model = Basket
        fields = ('customer', 'status')

#Basket Item Filter
class BasketItemFilter(filters.FilterSet):
    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")
