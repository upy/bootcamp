from django.contrib import admin

from payments.models import Bank, BankAccount


class BankAccountInline(admin.TabularInline):
    model = BankAccount
    extra = 1


# Bank model registered to the admin
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    inlines = [BankAccountInline, ]


# Bank Account registered to the admin
@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("bank", "name", "iban")
    list_display = ("bank", "name", "iban")
