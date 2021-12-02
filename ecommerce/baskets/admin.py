from django.contrib import admin
from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("customer", "status")
    search_fields = ("customer", "status")
    autocomplete_fields = ("customer",)


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("basket", "product", "quantity", "price")
    search_fields = ("basket", "product", "quantity", "price")
    autocomplete_fields = ("basket", "product")
