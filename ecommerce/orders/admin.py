from django.contrib import admin

from orders.forms import OrderAdminForm
from orders.models import Order, OrderItem, BillingAddress, ShippingAddress


class OrderItemInline(admin.TabularInline):
    """
    Inline for Order Item
    """
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin View for Order
    """
    list_display = ('customer', 'basket', 'total_price')
    list_filter = ('customer', )
    inlines = (OrderItemInline, )
    form = OrderAdminForm


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin View for OrderItem
    """
    list_display = ('order', 'product', 'price')


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    """
    Admin View for BillingAddress
    """
    list_display = ('full_name', 'line_1', 'line_2', 'phone', 'district', 'city')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    """
    Admin View for ShippingAddress
    """
    list_display = ('full_name', 'line_1', 'line_2', 'phone', 'district', 'city')