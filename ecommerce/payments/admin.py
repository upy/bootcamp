from django.contrib import admin
from .models import Bank, BankAccount


class BankAccountInline(admin.StackedInline):
    model = BankAccount


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("bank", "name", 'iban')
    search_fields = ("iban", "bank")
    autocomplete_fields = ("bank",)


@admin.register(Bank)
class AddressAdmin(admin.ModelAdmin):
    model = Bank
    list_display = ('name',)
    search_fields = ("name",)
    inlines = [BankAccountInline, ]
