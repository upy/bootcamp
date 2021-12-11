from django.db.transaction import atomic
from rest_framework import serializers

from products.models import Product, Category, Stock, Price


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ("id", "product", "quantity", "created_at", "modified_at")


class NestedStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ("id", "quantity")


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ("id", "product", "amount", "created_at", "modified_at")


class NestedPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ("id", "amount")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "sku", "name", "description", "color", "size", "categories", "stock", "price", "created_at",
                  "modified_at")


class NestedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "sku", "name", "color", "size", "categories", "price")


class ProductDetailedSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    stock = NestedStockSerializer()
    price = NestedPriceSerializer()

    class Meta:
        model = Product
        fields = (
            "id", "sku", "name", "description", "color", "size", "categories", "stock", "price", "created_at",
            "modified_at")

    @atomic()
    def create(self, validated_data):
        categories = validated_data.pop("categories", None)
        product = super().create(validated_data)
        if categories:
            serializer = CategorySerializer(data=categories, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            product.categories.add(*serializer.instance)
        return product


