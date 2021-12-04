from django.contrib import admin

from basket.models import Basket, BasketItem

# class StockInline(admin.StackedInline):
#     #model = Stock
#
#
from orders.models import Order


class BasketItemInLine(admin.StackedInline):
    model = BasketItem


class OrderInLine(admin.StackedInline):
    model = Order


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer__email",)
    list_display = ("id", "customer", "status")
    inlines = [BasketItemInLine, OrderInLine]


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    search_fields = ("basket__id", "product__id")
    list_display = ("basket", "product")
    autocomplete_fields = ("basket", "product")
