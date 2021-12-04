from django.contrib import admin

from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ("customer__first_name", "customer__last_name", "customer__email")
    list_display = ("customer", "status")
    list_filter = ("status",)


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    search_fields = ("basket__customer__name", "product__name")
    list_display = ("basket", "product", "quantity", "price")
