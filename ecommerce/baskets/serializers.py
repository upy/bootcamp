from decimal import Decimal

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from baskets.models import BasketItem, Basket
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer, ProductDetailedSerializer


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("customer", "status", "slug")


class BasketItemDetailedSerializer(BasketItemSerializer):
    product = ProductDetailedSerializer()
    total = serializers.SerializerMethodField()

    class Meta(BasketItemSerializer.Meta):
        fields = BasketItemSerializer.Meta.fields + ("total",)

    def get_total(self, obj):
        return obj.price * obj.quantity


class BasketDetailedSerializer(BasketSerializer):
    basketitem_set = BasketItemDetailedSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta(BasketSerializer.Meta):
        fields = BasketSerializer.Meta.fields + ("basketitem_set", "total")

    def get_total(self, obj):
        item_set = obj.basketitem_set.all()
        total = Decimal("0")
        for item in item_set:
            total += item.price * item.quantity
        return total


class BasketItemValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ("product", "quantity")

    def validate(self, attrs):
        attrs = super().validate(attrs)
        product = attrs.get("product")
        quantity = attrs.get("quantity")
        try:
            stock = product.stock
        except Exception:
            raise ValidationError(detail={"product": _("Stock not found")})
        if stock.quantity < 1:
            raise ValidationError(detail={"product": _("Stock not found")})
        if stock.quantity < quantity:
            raise ValidationError(detail={"product": _("Stock not found")})
        return attrs

