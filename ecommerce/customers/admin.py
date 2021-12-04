from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from customers.models import Customer, Address, Country, City


class AddressInLine(admin.StackedInline):
    model = Address


class CityInLine(admin.StackedInline):
    model = City


class CountryInline(admin.StackedInline):
    model = Country


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
    inlines = [AddressInLine]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name", "country")
    list_display = ("name", "country")
    autocomplete_fields = ("country", )
    # inlines = [CountryInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ("name", "full_name", "city", "customer", "line_one", "line_two")
    list_display = ("name", "full_name", "customer", "city", "post_code")
    autocomplete_fields = ("city",)
    # inlines = [CountryInline, CityInLine]
