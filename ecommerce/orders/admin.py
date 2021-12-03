from django.contrib import admin

from orders.models import BillingAddress, InvoiceAddress, OrderBankAccount, Order, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line1", "line2", "city")
    search_fields = ("full_name", "city")


@admin.register(InvoiceAddress)
class InvoiceAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line1", "line2", "city")
    search_fields = ("full_name", "city")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "bank", "iban")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "basket", "total_price")
    search_fields = ("customer__full name",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price")
    search_fields = ("product__sku", "product__name")
