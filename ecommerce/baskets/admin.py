from django.contrib import admin
from baskets.models import Basket, BasketItem

# Register your models here.


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer", "status")
    list_display = ("customer", "status",)
    autocomplete_fields = ("customer",)

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    search_fields = ("basket",)
    list_display = ("basket", "product","quantity", "price")
