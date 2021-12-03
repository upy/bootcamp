from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from customers.models import Customer, Address, Country, City


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("name", "line1", "line2", "city")
    search_fields = ("name", "city")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country")

