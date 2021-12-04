from django.contrib import admin

from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("customer", "status")


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    search_fields = ("product", "quantity")
