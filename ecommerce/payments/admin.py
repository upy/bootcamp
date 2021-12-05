from django.contrib import admin

from payments.models import Bank, BankAccount


class BankAccountInline(admin.TabularInline):
    """
    Inline for BankAccounts
    """
    model = BankAccount
    extra = 1


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    """
    Admin View for Bank
    """
    list_display = ('name', )
    inlines = [BankAccountInline, ]


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    """
    Admin View for BankAccount
    """
    list_display = ('name', 'iban')