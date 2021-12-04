from django.contrib import admin

from orders.models import BillingAddress, InvoiceAddress, Order, OrderBankAccount, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name",)


@admin.register(InvoiceAddress)
class InvoiceAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_price")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "bank_name")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product", "order", "price")