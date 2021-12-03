from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from orders.models import BillingAddress, InvoiceAddress, Order, OrderBankAccount, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line_1", "line_2", "phone", "district", "postcode", "city")
    search_fields = ("full_name", "line_1", "line_2", "phone", "city__name", "city__country__name")


@admin.register(InvoiceAddress)
class InvoiceAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line_1", "line_2", "phone", "district", "postcode", "city")
    search_fields = ("full_name", "line_1", "line_2", "phone", "city__name", "city__country__name")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "basket", "billing_address", "shipping_address", "total_price")
    search_fields = ("customer__first_name", "basket__customer__first_name")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "iban", "bank_name", "order")
    search_fields = ("name", "iban", "bank_name")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price")
    search_fields = ("product__sku", "product__name")
