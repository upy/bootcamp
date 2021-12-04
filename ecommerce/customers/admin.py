from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from customers.models import Customer, Address, City, Country


class CityInline(admin.TabularInline):
    model = City


class CountryInline(admin.TabularInline):
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


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("customer", "name", "city")
    list_filter = ("city",)
    search_fields = ("line_1", "line_2", "city")
    # inlines = (CityInline, CountryInline) #TODO: Add inlines


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    list_filter = ("country",)
    search_fields = ("city",)
    # inlines = (CountryInline,) #TODO: Add inlines


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)