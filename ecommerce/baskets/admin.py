from django.contrib import admin

from baskets.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("customer", "status")
    search_fields = ("customer", "status" )


@admin.register(BasketItem)
class BasketItem(admin.ModelAdmin):
    list_display = ("basket", "product", "quantity", "price", )

# Register your models here.
