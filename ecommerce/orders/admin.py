from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin View for Order
    """
    list_display = ('customer', 'basket', 'total_price')
    list_filter = ('customer', )
    inlines = (OrderItemInline, )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin View for OrderItem
    """
    list_display = ('order', 'product', 'price')
