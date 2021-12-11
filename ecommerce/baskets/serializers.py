from rest_framework import serializers

from baskets.models import Basket


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("__all__")

