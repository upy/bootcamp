from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from customers.models import Customer, Country, City, Address


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


class AddressInline(admin.StackedInline):
    model = Address


class CityInline(admin.StackedInline):
    model = City


@admin.register(Address)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "phone")
    list_display = ("name", "full_name", "line1", "line2", "phone", "district", "post_code", "city")


@admin.register(City)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "country",)
    inlines = [AddressInline]


@admin.register(Country)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    inlines = [CityInline]
