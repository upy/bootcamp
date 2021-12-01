from django.contrib import admin

from orders.models import BillingAddress, InvoiceAddress, Order, OrderBankAccount, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)
    list_display = ("full_name", "line_1", "line_2")


@admin.register(InvoiceAddress)
class InvoiceAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)
    list_display = ("full_name", "line_1", "line_2")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_price")
    search_fields = ("customer__full_name", )


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "bank", "iban")
    search_fields = ("name", )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price")
    search_fields = ("product__name", "product__sku",)
