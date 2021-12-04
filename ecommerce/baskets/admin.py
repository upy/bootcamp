from django.contrib import admin
from baskets.models import Basket, BasketItem

# Register your models here.


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("customer", "status")
    search_fields = ("customer", "status")
    filter = ("status", )


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("basket", "product", "quantity", "price")
