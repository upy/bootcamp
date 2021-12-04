from django.contrib import admin

from products.models import Product, Stock, Price, Category


class StockInline(admin.StackedInline):
    model = Stock


class PriceInline(admin.StackedInline):
    model = Price


class CategoryInline(admin.StackedInline):
    model = Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "sku")
    list_display = ("sku", "name", "color", "size", "all_categories")
    inlines = [StockInline, PriceInline]

    def all_categories(self, obj):
        return "\n".join([p.name for p in obj.categories.all()])


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
