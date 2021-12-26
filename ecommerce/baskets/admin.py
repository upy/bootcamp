from django.contrib import admin

from baskets.models import Basket, BasketItem


class BasketItemInline(admin.TabularInline):
    """
    Inline class for BasketItem
    """

    model = BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    """
    Admin view for Basket
    """

    list_display = ("customer", "status")
    inlines = [
        BasketItemInline,
    ]


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    """
    Admin view for BasketItem
    """

    list_display = ("basket", "product", "quantity", "price")
    search_fields = ("product__sku", "product__name")
