from django.contrib import admin

from payments.models import Bank, BankAccount

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("name", )

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("bank","name","iban" )
