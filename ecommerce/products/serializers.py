from django.db.transaction import atomic
from rest_framework import serializers

from products.models import Product, Category, Stock, Price


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "sku", "name", "description", "color", "size", "categories", "created_at", "modified_at")


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name", )


class ProductDetailedSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "sku", "name", "description", "color", "size", "categories", "created_at", "modified_at")

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


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ("product", "quantity")


class StockDetailedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Stock
        fields = ("product", "quantity")


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ("product", "amount")


class PriceDetailedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Price
        fields = ("product", "amount")
