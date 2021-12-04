from django.contrib import admin

from baskets.models import Basket, BasketItem


class BasketItemInline(admin.TabularInline):
    model = BasketItem
    # extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status')
    inlines = (BasketItemInline, )


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('basket', 'product', 'quantity', 'price')