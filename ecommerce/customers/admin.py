from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from customers.models import Customer, Country, City, Address
from orders.models import ShippingAddress, BillingAddress


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


class CityInline(admin.StackedInline):
    model = City


class ShippmentAddressInline(admin.StackedInline):
    model = ShippingAddress


class BillingAddressInline(admin.StackedInline):
    model = BillingAddress


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name")
    inlines = [CityInline, ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name", "country__name")
    list_display = ("name", "country")
    autocomplete_fields = ("country",)
    # inlines = [BillingAddressInline, ShippingAddressInLine ]
