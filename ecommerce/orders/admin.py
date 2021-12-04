from django.contrib import admin

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "district", "city", "line_one")
    list_display = ("full_name", "post_code","district", "city")
    autocomplete_fields = ("city",)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "district", "city", "line_one")
    list_display = ("full_name", "post_code","district", "city")
    autocomplete_fields = ("city",)


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "iban", "bank_name")
    list_display = ("name", "bank_name", "iban")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("customer",)
    list_display = ("customer", "billing_address", "shipping_address", "total_price" )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ("order", "product")
    list_display = ("order", "product", "price")