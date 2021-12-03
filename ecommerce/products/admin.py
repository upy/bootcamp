from django.contrib import admin

from products.models import Product, Stock, Price


class StockInline(admin.StackedInline):
    model = Stock


class PriceInline(admin.StackedInline):
    model = Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Register the Product model to admin panel
    """
    search_fields = ("name", "sku")
    list_display = ("sku", "name", "color", "size")
    inlines = [StockInline, PriceInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    """
    Register the Stock model to admin panel
    """
    list_display = ("product", "quantity")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product", )


@admin.register(Price)
class StockAdmin(admin.ModelAdmin):
    """
    Register the Price model to admin panel
    """
    list_display = ("product", "amount")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product", )
