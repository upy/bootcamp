from django.db.models import F, Sum
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from baskets.enums import BasketStatus
from baskets.models import Basket
from customers.models import Address
from customers.serializers import CitySerializer
from orders.models import (
    BillingAddress,
    Order,
    OrderBankAccount,
    OrderItem,
    ShippingAddress,
)
from payments.models import BankAccount
from products.models import Stock
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "price")

    def validate(self, attrs):
        attrs = super().validate(attrs)
        price = attrs["price"]
        product = attrs["product"]
        if product.price.amount != price:
            raise ValidationError(detail={"product": _("Price changed")})
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "basket",
            "status",
            "billing_address",
            "shipping_address",
            "total_price",
        )


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = (
            "id",
            "full_name",
            "line_1",
            "line_2",
            "phone",
            "district",
            "zipcode",
            "city",
        )


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            "id",
            "full_name",
            "line_1",
            "line_2",
            "phone",
            "district",
            "zipcode",
            "city",
        )


class OrderBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order")


class OrderItemDetailedSerializer(OrderItemSerializer):
    product = ProductSerializer()


class OrderDetailedSerializer(OrderSerializer):
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()
    orderitem_set = OrderItemDetailedSerializer(many=True)
    orderbankaccount_set = OrderBankAccountSerializer(many=True)

    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + (
            "orderitem_set",
            "orderbankaccount_set",
        )


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()


class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CitySerializer()


class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CitySerializer()


class CreateOrderSerializer(serializers.Serializer):
    basket = serializers.SlugRelatedField(
        slug_field="slug", queryset=Basket.objects.all()
    )
    billing_address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
    shipping_address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all()
    )
    bank_account = serializers.PrimaryKeyRelatedField(
        queryset=BankAccount.objects.all()
    )

    class Meta:
        fields = ("basket", "billing_address", "shipping_address", "bank_account")

    def validate(self, attrs):
        attrs = super().validate(attrs)
        customer = self.context["request"].user
        basket = attrs["basket"]
        billing_address = attrs["billing_address"]
        shipping_address = attrs["shipping_address"]
        if basket.customer != customer:
            raise ValidationError(detail={"basket": _("Invalid basket")})

        if shipping_address.customer != customer:
            raise ValidationError(detail={"basket": _("Invalid shipping address")})

        if billing_address.customer != customer:
            raise ValidationError(detail={"basket": _("Invalid billing address")})

        return attrs

    @atomic()
    def create(self, validated_data):
        customer = self.context["request"].user
        basket = validated_data["basket"]

        address_for_shipping = validated_data["shipping_address"]
        shipping_serializer = ShippingAddressSerializer(
            data={
                "full_name": address_for_shipping.full_name,
                "line_1": address_for_shipping.line_1,
                "line_2": address_for_shipping.line_2,
                "phone": address_for_shipping.phone,
                "district": address_for_shipping.district,
                "city": address_for_shipping.city_id,
                "zipcode": address_for_shipping.zipcode,
            }
        )
        shipping_serializer.is_valid(raise_exception=True)
        shipping_address_instance = shipping_serializer.save()

        address_for_billing = validated_data["billing_address"]
        billing_serializer = BillingAddressSerializer(
            data={
                "full_name": address_for_billing.full_name,
                "line_1": address_for_billing.line_1,
                "line_2": address_for_billing.line_2,
                "phone": address_for_billing.phone,
                "district": address_for_billing.district,
                "city": address_for_billing.city_id,
                "zipcode": address_for_billing.zipcode,
            }
        )
        billing_serializer.is_valid(raise_exception=True)
        billing_address_instance = billing_serializer.save()

        order_serializer = OrderSerializer(
            data={
                "customer": customer.id,
                "billing_address": billing_address_instance.id,
                "shipping_address": shipping_address_instance.id,
                "basket": basket.id,
                "total_price": 0,
            }
        )
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save()

        bank_account = validated_data["bank_account"]
        bank_account_serializer = OrderBankAccountSerializer(
            data={
                "bank_name": bank_account.bank.name,
                "name": bank_account.name,
                "iban": bank_account.iban,
                "order": order.id,
            }
        )
        bank_account_serializer.is_valid(raise_exception=True)
        bank_account_serializer.save()

        for basket_item in basket.basketitem_set.all():
            for i in range(basket_item.quantity):
                order_item_serializer = OrderItemSerializer(
                    data={
                        "order": order.id,
                        "product": basket_item.product_id,
                        "price": basket_item.price,
                    }
                )
                order_item_serializer.is_valid(raise_exception=True)
                order_item_serializer.save()
            stock = basket_item.product.stock
            Stock.objects.filter(id=stock.id).update(
                quantity=F("quantity") - basket_item.quantity
            )
        basket.status = BasketStatus.SUBMITTED
        basket.save(update_fields=["status", "modified_at"])
        values = (
            order.orderitem_set.values("order")
            .annotate(total=Sum("price"))
            .values("total")
        )
        order.total_price = values[0]["total"]
        order.save(update_fields=["total_price"])
        return order

    def to_representation(self, instance):
        serializer = OrderDetailedSerializer()
        return serializer.to_representation(instance)
