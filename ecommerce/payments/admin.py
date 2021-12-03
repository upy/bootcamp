from django.contrib import admin
from payments.models import Bank, BankAccount
# Register your models here.


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter = ("name", )


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("bank", "name")
    search_fields = ("bank", "name")
    filter = ("bank", )
