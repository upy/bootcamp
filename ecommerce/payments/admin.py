from django.contrib import admin


from payments.models import Bank, BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", )


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("bank", "name", "iban")
    list_display = ("bank", "name", "iban")
