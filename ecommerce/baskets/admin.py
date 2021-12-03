from django.contrib import admin
from .models import Basket, BasketItem


class BasketItemInline(admin.TabularInline):
    model = BasketItem
    fields = ('product', 'quantity', 'price')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('status',)
    inlines = [BasketItemInline, ]
