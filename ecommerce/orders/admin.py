from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    """
    Register the BillingAddress model to admin panel
    """
    list_display = ("full_name", "district")
    search_fields = ("full_name", "district")
    ordering = ("full_name",)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    """
    Register the ShippingAddress model to admin panel
    """
    list_display = ("full_name", "district")
    search_fields = ("full_name", "district")
    ordering = ("full_name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Register the Order model to admin panel
    """
    list_display = ("customer", "total_price")
    search_fields = ("customer", "total_price")
    ordering = ("total_price",)


@admin.register(OrderBankAccount)
class OrderBankAccountAdmin(admin.ModelAdmin):
    """
    Register the OrderBankAccount model to admin panel
    """
    list_display = ("name", "bank_name")
    search_fields = ("name", "bank_name")
    ordering = ("name",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Register the OrderItem model to admin panel
    """
    list_display = ("order", "price")
    search_fields = ("order", "price")
    ordering = ("price",)
