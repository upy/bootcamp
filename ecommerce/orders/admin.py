from django.contrib import admin

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, \
    Order, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ["full_name", "district", "postcode", "city"]
    list_display = ["full_name", "line_1", "line_2", "phone", "district",
                    "postcode", "city"]
    autocomplete_fields = ["city", ]


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ["full_name", "district", "postcode", "city"]
    list_display = ["full_name", "line_1", "line_2", "phone", "district",
                    "postcode", "city"]


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "iban", "bank_name", "order")
    list_display = ("name", "iban", "bank_name", "order")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["customer"]
    list_display = ["customer", "basket", "billing_address", "shipping_address",
                    "total_price"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ["order", "product"]
    list_display = ["order", "product", "price"]
