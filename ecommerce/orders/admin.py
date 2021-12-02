from django.contrib import admin

from orders.models import BillingAddress, ShippingAddress, Order, OrderBankAccount, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "phone")
    list_display = ("full_name", "line1", "line2", "phone", "district", "post_code", "city")


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "phone")
    list_display = ("full_name", "line1", "line2", "phone", "district", "post_code", "city")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("customer", "basket")
    list_display = ("customer", "basket", "billing_address", "shipping_address", "total_price")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "bank")
    list_display = ("name", "bank", "iban", "order")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ("order", "product")
    list_display = ("order", "product", "total_price")



