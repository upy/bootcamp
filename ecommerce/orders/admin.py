from django.contrib import admin

# Register your models here.
from orders.models import BillingAddress, InvoiceAddress, OrderBankAccount, Order


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("fullName", "line1", "city")
    search_fields = ("city", "city__country")

@admin.register(InvoiceAddress)
class InvoiceAddressAdmin(admin.ModelAdmin):
    list_display = ("fullName", "line1", "city")
    search_fields = ("city", "city__country")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "iban", "bank_name")
    list_display = ("name", "bank_name", "iban")
    list_filter = ("bank_name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("customer",)
    list_display = ("customer", )