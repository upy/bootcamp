from django.contrib import admin

from payments.models import Bank, BankAccount


class BankAccountInLine(admin.StackedInline):
    model = BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    #inlines = [BankAccountInLine]


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("bank", "name", "iban")
    list_display = ("bank", "name", "iban")

