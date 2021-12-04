from django.contrib import admin

from payments.models import Bank, BankAccount


class BankAccountInLine(admin.StackedInline):
    model = BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    inlines = [BankAccountInLine, ]


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "bank_name", "customer__email")
    list_display = ("name", "bank", "iban")
    autocomplete_fields = ("bank", "customer")
