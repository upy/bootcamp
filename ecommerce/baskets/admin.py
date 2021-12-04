from django.contrib import admin

from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer__name",)
    list_display = ("customer", "status")
    list_filter = ("status",)


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    search_fields = ("product__name", "basket", "product__name")
    list_display = ("product", "basket", "quantity", "price")
