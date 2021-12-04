from django.contrib import admin

from customers.admin import AddressAdmin
from orders.models import Order, OrderItem, OrderBankAccount, BillingAddress, ShippingAddress


@admin.register(BillingAddress)
class BillingAddressAdmin(AddressAdmin):
    pass


@admin.register(ShippingAddress)
class ShippingAddressAdmin(AddressAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("customer", "created_at")
    list_display = ("customer", "created_at", "total_price")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ("product__name", "order__customer__email")
    list_display = ("product", "order", "price")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "order__customer__email")
    list_display = ("order", "name", "bank_name")
