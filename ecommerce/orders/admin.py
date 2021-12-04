from django.contrib import admin
from orders.models import ShippingAddress, BillingAddress, Order, OrderItem, OrderBankAccount

# Register your models here.


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("city", "district")


@admin.register(BillingAddress)
class BillingAddressAddressAdmin(admin.ModelAdmin):
    list_display = ("city", "district")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "basket")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("bank", "name")
