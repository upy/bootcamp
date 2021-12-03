from django.contrib import admin
from . models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    """
    Register the Basket model to admin panel
    """
    list_display = ("customer", "status")
    search_fields = ("customer__first_name", "customer__last_name", "status")
    ordering = ("status", )


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    """
    Register the BasketItem model to admin panel
    """
    list_display = ("product",)
    search_fields = ("product__name", )
    ordering = ("product", )
