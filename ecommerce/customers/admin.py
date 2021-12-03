from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from . models import Customer, Country, City, Address


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


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Register the Country model to admin panel
    """
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Register the City model to admin panel
    """
    list_display = ("name", "country")
    search_fields = ("name", "country")
    ordering = ("name",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Register the Address model to admin panel
    """
    list_display = ("name", "city")
    search_fields = ("name", "city")
    ordering = ("name",)
