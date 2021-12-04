from django.contrib import admin

from payments.models import Bank, BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name", "customer__email", "bank__name")
    list_display = ("name", "customer", "bank")
