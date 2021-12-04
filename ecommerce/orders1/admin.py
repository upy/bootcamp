from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from orders.models import BillingAddress, ShippingAddress, Order, OrderBankAccount, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line_1", "line_2", "phone", "district", "postcode", "city")
    search_fields = ("full_name", "line_1", "line_2", "phone", "district", "postcode",
                     "city__name", "city__country__name")
    autocomplete_fields = ("city",)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line_1", "line_2", "phone", "district", "postcode", "city")
    search_fields = ("full_name", "line_1", "line_2", "phone", "district", "postcode",
                     "city__name", "city__country__name")
    autocomplete_fields = ("city",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "basket", "billing_address", "shipping_address", "total_price")
    search_fields = ("full_name", "line_1", "line_2", "phone", "district", "postcode",
                     "city__name", "city__country__name")
    autocomplete_fields = ("customer", "basket", "billing_address", "shipping_address")


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "iban", "bank_name", "order")
    search_fields = ("name", "iban", "bank_name", "order")
    autocomplete_fields = ("order",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price")
    search_fields = ("order", "product", "price")
    autocomplete_fields = ("order", "product", "price")