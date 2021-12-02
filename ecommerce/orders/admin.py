from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from orders.models import BillingAddress, InvoiceAddress,OrderBankAccount,Order, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("fullname","phone")
    list_display = ("fullname", )

@admin.register(InvoiceAddress)
class InvoiceAddressAdmin(admin.ModelAdmin):
    search_fields = ("fullname","phone")
    list_display = ("fullname",)

@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "bank_name", "order")
    search_fields = ("customer__fullname",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "basket","total_price")
    search_fields = ("name",)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "total_price")
    search_fields = ("product__name", "product__sku",)