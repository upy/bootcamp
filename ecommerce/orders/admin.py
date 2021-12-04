from django.contrib import admin

from orders.models import BillingAddress , ShippingAddress , OrderBankAccount , Order,OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderBankAccountInline(admin.TabularInline):
    model = OrderBankAccount


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name","city")
    list_display = ("full_name","city")


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ("full_name","city")
    list_display = ("full_name","city")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'basket', 'total_price')
    search_fields = ('customer', )
    inlines = (OrderItemInline, )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order","product", "price")
    search_fields = ("order","product")

@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    list_display = ("name","bank_name")
    search_fields = ("name", )
