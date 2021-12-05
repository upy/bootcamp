from django.contrib import admin

from orders.models import BillingAddress, Order, OrderBankAccount, OrderItem, ShippingAddress


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_price")
    search_fields = ("customer__full_name",)
    autocomplete_fields = ("billing_address", "shipping_address")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price")
    search_fields = ("product__name", "product__sku",)
    autocomplete_fields = ("order", "product")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "bank_name", "iban")
    search_fields = ("name",)


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)
    list_display = ("full_name", "line_1", "line_2")
    autocomplete_fields = ("city",)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)
    list_display = ("full_name", "line_1", "line_2")
    autocomplete_fields = ("city",)
