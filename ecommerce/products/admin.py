from django.contrib import admin

from products.models import Category, Price, Product, Stock


class StockInline(admin.StackedInline):
    """
    Inline class for Stock model
    """

    model = Stock


class PriceInline(admin.StackedInline):
    """
    Inline class for Price
    """

    model = Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """

    search_fields = ("name", "sku")
    list_display = ("sku", "name", "color", "size")
    inlines = [StockInline, PriceInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    """
    Stock admin
    """

    list_display = ("product", "quantity")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product",)


@admin.register(Price)
class StockAdmin(admin.ModelAdmin):
    """
    Price admin
    """

    list_display = ("product", "amount", "created_at", "modified_at")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin
    """

    list_display = ("name",)
    search_fields = ("name",)
