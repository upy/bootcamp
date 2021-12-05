from django.contrib import admin

from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer", )
    list_filter = ("basket_status", )
    list_display = ("customer", "basket_status")


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "price")
