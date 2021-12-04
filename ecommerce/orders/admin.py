from django.contrib import admin

from orders.models import Order,OrderItem,OrderBankAccount,BillingAddress,ShippingAddress


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line_1", "line_2", "district", "postcode", "city",)
    search_fields = ("full_name", "district", "city")


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "line_1", "line_2", "district", "postcode", "city",)
    search_fields = ("full_name", "district", "city")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "basket" , "billing_address", "shipping_address", "total_price")
    search_fields = ("customer", )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price", )
    search_fields = ("order", "product", )


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "iban", "order", "bank_name", )
    search_fields = ("name", "iban", "order", "bank_name", )

# Register your models here.
