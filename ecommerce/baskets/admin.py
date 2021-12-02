from django.contrib import admin

from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer", "status")
    list_display = ("customer", "status")


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    search_fields = ("product__name", "basket__customer", "product__sku")
    list_display = ("product", "quantity")
