from django.contrib import admin

from payments.models import Bank, BankAccounts


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(BankAccounts)
class BankAccountsAdmin(admin.ModelAdmin):
    list_display = ("bank", "name", "iban", )
    search_fields = ("bank", "name", "iban", )

# Register your models here.
