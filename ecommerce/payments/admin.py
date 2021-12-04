from django.contrib import admin

from payments.models import Bank, BankAccount


class BankAccountInline(admin.TabularInline):
    model = BankAccount
    extra = 1

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = (BankAccountInline, )


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'iban')