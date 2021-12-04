from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from customers.models import Customer, Country, City, Address


class CityInline(admin.StackedInline):
    model = City


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


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name", "country__name")
    list_display = ("name", "country")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    inlines = [CityInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ("name", "line1", "line2", "phone_number", "district", "postcode", "city__name")
    list_display = ("name", "line1", "line2", "phone_number", "district", "postcode", "city")
