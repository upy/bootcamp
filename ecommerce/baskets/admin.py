from django.contrib import admin

from baskets.models import Basket, BasketItem


class BasketItemInline(admin.StackedInline):
    model = BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer", "status")
    list_display = ("customer", "status")
    inlines = [BasketItemInline]


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    search_fields = ("basket", "product")
    list_display = ("basket", "product", "quantity", "price")
