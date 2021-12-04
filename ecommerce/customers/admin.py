from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from customers.models import Address, Customer


class AddressInline(admin.StackedInline):
    model = Address


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
    inlines = (AddressInline,)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "customer", "address_type", "full_name", "line_1", "line_2",
        "phone", "district", "postcode", "city"
    )
    search_fields = (
        "district", "postcode", "city__name", "customer__first_name",
    )
    autocomplete_fields = ("customer", )
