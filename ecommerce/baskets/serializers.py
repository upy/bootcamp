from rest_framework import serializers

from baskets.models import Basket
from customers.serializers import CustomerSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("id", "customer", "status")

class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()
