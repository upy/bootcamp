from django.contrib import admin
from baskets.models import Basket, BasketItem


class BasketItemInline(admin.TabularInline):
    model = BasketItem
    fields = ('product', 'quantity', 'price')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('status',)
    inlines = [BasketItemInline, ]


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price')
    search_fields = ("product__name",)
