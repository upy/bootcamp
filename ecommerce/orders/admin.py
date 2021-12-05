from django.contrib import admin

from orders.models import BillingAddress, ShippingAddress, OrderBankAccount, \
    Order, OrderItem


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ["full_name", "district", "postcode", "city__name", "city__country__name"]
    list_display = ["full_name", "line_1", "line_2", "phone", "district",
                    "postcode", "city"]
    autocomplete_fields = ["city", ]


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ["full_name", "district", "postcode", "city__name", "city__country__name"]
    list_display = ["full_name", "line_1", "line_2", "phone", "district",
                    "postcode", "city"]


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "iban", "bank_name", "order__customer__email", "order__basket__basket_status")
    list_display = ("name", "iban", "bank_name", "get_basket_status", "get_email")

    @admin.display(description='email')
    def get_email(self, obj):
        return obj.order.customer.email

    @admin.display(description='Status')
    def get_basket_status(self, obj):
        return obj.order.basket.basket_status


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["customer__email",
                     "basket__basket_status",
                     "billing_address__city__name",
                     "billing_address__city__country__name",
                     "billing_address__district",
                     "shipping_address__city__name",
                     "shipping_address__city__country__name",
                     "shipping_address__district",
                     "total_price",]
    list_display = ["customer",
                    "get_basket_status",
                    "billing_address",
                    "shipping_address",
                    "total_price",]

    @admin.display(description='Basket Status')
    def get_basket_status(self, obj):
        return obj.basket.basket_status


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ["order__customer__email",
                     "product",
                     "price",
                     "order__basket__basket_status"]
    list_display = ["order", "product", "price", "get_basket_status"]

    @admin.display(description='Basket Status')
    def get_basket_status(self, obj):
        return obj.order.basket.basket_status
