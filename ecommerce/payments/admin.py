from django.contrib import admin

from payments.models import Bank, BankAccount


class BankAccountInline(admin.StackedInline):
    model = BankAccount


@admin.register(Bank)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    inlines = [BankAccountInline]


@admin.register(BankAccount)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "iban")
    list_display = ("name", "iban", "bank")

