from django.contrib import admin

# Register your models here.
from basket.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("customer", "status")
    search_fields = ("customer__first_name", "customer__last_name")
    autocomplete_fields = ("customer", )


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("basket", "product")
    search_fields = ("product__name",)
