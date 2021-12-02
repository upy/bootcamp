from django.contrib import admin

from orders.models import BillingAddress, Order, OrderBankAccount, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_price")
    search_fields = ("customer__full_name", )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price")
    search_fields = ("product__name", "product__sku",)


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "bank_name", "iban")
    search_fields = ("name",)


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)
    list_display = ("full_name", "line_1", "line_2")
