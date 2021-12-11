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
        fields = ("id", "name",)


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


# Stock Serializer
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'product', 'quantity')


# Stock Detailed Serializer - nested serializer
class StockDetailedSerializer(StockSerializer):
    products = ProductSerializer()


# Price Serializer
class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ("product", "amount")


# Price Detailed Serializer - nested serializer
class PriceDetailedSerializer(PriceSerializer):
    products = ProductSerializer()
