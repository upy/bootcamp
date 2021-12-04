from django.contrib import admin

from products.models import Product, Stock, Price, Category, Categorization


class StockInline(admin.StackedInline):
    model = Stock


class PriceInline(admin.StackedInline):
    model = Price


class CategorizationInline(admin.StackedInline):
    model = Categorization


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "sku")
    list_display = ("sku", "name", "color", "size")
    inlines = [StockInline, PriceInline, CategorizationInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "productList")
    search_fields = ("name",)
    inlines = [CategorizationInline,]


@admin.register(Categorization)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "product")
    search_fields = ("product__name", "product__sku", "category__name")


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product",)


@admin.register(Price)
class StockAdmin(admin.ModelAdmin):
    list_display = ("product", "amount")
    search_fields = ("product__name", "product__sku")
    autocomplete_fields = ("product",)
