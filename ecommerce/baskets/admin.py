from django.contrib import admin

from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    search_fields = ["customer__email", "basket_status"]
    list_filter = ("basket_status", )
    list_display = ("customer", "basket_status")


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("basket", "product", "quantity", "price")
    search_fields = ("basket__customer__email",
                     "basket__basket_status",
                     "product__sku",
                     "product__name",
                     "quantity",
                     "price")
