from django.contrib import admin

from payments.models import Bank, BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(BankAccount)
class BankAccountsAdmin(admin.ModelAdmin):
    list_display = ("bank", "name", "iban", )
    search_fields = ("bank", "name", "iban", )
