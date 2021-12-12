from rest_framework import serializers
from baskets.models import Basket, BasketItem


class BasketSerializers(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = "__all__"


class BasketItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = "__all__"
