from django.contrib import admin
from orders.models import Order, OrderItem, OrderBankAccount, ShippingAddress, BillingAddress
from payments.admin import BankAccountAdmin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "basket","billing_address", "shipping_address", "total_price", )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product", "price",)

@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(BankAccountAdmin): # Inherited from payments app admin BankAccountAdmin
    list_display = ("name", "iban", "bank",)

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("name", "line1", "line2", "district", "city", "postal_code",)

@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("name", "line1", "line2", "district", "city", "postal_code",)