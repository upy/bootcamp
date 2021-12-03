from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Bank, BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    """
    Register the Bank model to admin panel
    """
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    """
    Register the BankAccount model to admin panel
    """
    list_display = ("name", "bank")
    search_fields = ("name", "bank")
    ordering = ("name", )
