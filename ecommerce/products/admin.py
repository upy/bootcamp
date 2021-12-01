from django.contrib import admin

from products.models import Product, Stock, Price, Category


class StockInline(admin.StackedInline):
    model = Stock


class PriceInline(admin.StackedInline):
    model = Price


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("product__name", "product__sku")
    list_display = ("name",)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "sku")
    list_display = ("sku", "name", "color", "size")
    inlines = [StockInline, PriceInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product", )


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("product", "amount")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product", )
