from django.contrib import admin

from orders.models import BillingAddress, ShippingAddress, Order, OrderBankAccount, OrderItem


class OrderInLine(admin.StackedInline):
    model = Order


class OrderItemInLine(admin.StackedInline):
    model = OrderItem


class OrderBankAccountInLine(admin.StackedInline):
    model = OrderBankAccount


@admin.register(BillingAddress, ShippingAddress)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ("name", "city__name", "customer__email")
    list_display = ("name", "full_name", "line1", "line2", "phone_number", "district", "post_code", "city", "customer")
    autocomplete_fields = ("city", "customer")
    inlines = [OrderInLine, ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("customer__email", "basket__status", "billing_address__name", "shipping_address__name")
    list_display = ("customer", "basket", "billing_address", "shipping_address", "total_price")
    autocomplete_fields = ("customer", "basket", "billing_address", "shipping_address")
    inlines = [OrderItemInLine, OrderBankAccountInLine]


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("iban", "order__id", "order__customer__email")
    list_display = ("iban", "bank_name", "order")
    autocomplete_fields = ("order", )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ("product__name", "product__sku" "order__id", "order__customer__email")
    list_display = ("product", "order", "price")
    autocomplete_fields = ("order", )
