from django.contrib import admin

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, Order, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "district", "city", "line_one", "line_two")
    list_display = ("full_name", "district", "city", "post_code")
    list_filter = ("city",)
    autocomplete_fields = ("city",)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "district", "city", "line_one", "line_two")
    list_display = ("full_name", "district", "city", "post_code")
    list_filter = ("city",)
    autocomplete_fields = ("city",)


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "iban", "bank_name")
    list_display = ("name", "bank_name", "iban")
    list_filter = ("bank_name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("customer",)
    list_display = ("customer", )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ("order", "product", "price")
    list_display = ("get_customer_name", "get_product_name", "price")

    @admin.display(description="Customer Name")
    def get_customer_name(self, obj):
        return ("%s %s" % (obj.order.customer.first_name, obj.order.customer.last_name)).upper()

    @admin.display(description="Product Name")
    def get_product_name(self, obj):
        return obj.product.name
