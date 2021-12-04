from django.contrib import admin

from payments.models import Bank, BankAccount

#Bank model registered to the admin
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)

#Bank Account registered to the admin
@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("bank", "name", "iban")
    list_display = ("bank", "name", "iban")