from django.contrib import admin

from baskets.models import Basket, BasketItem

# Register your models here.

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer", )
    list_filter = ("customer", "status", )
    list_display = ("customer", "status")


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("product", "basket", "quantity", "price")
