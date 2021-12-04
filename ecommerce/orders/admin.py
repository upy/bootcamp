from django.contrib import admin

from .models import Order, OrderItem, OrderBankAccount, BillingAddress, ShippingAddress


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderBankAccountInline(admin.TabularInline):
    model = OrderBankAccount


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("customer", "shipping_address")
    list_display = ("customer", "basket", "billing_address", "shipping_address", "total_price")
    lines = [OrderItemInline, OrderBankAccountInline]


@admin.register(OrderItem)
class OrderItemInline(admin.ModelAdmin):
    model = OrderItem
    search_fields = ("product", )
    list_display = ("product", "price",)


@admin.register(OrderBankAccount)
class OrderBankAccountInline(admin.ModelAdmin):
    product = OrderBankAccount
    search_fields = ("bank_name", "order")
    list_display = ("bank_name", "order")


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line1", "line2", "phone_number", "district", "postal_code",)
    search_fields = ("full_name", "phone", "name", "postal_code")


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line1", "line2", "phone_number", "district", "postal_code",)
    search_fields = ("full_name", "phone", "postal_code",)

