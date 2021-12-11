from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from customers.models import Customer, City, Country, Address


class CustomerFilter(filters.FilterSet):
    first_name = filters.CharFilter(label=_("First Name"),
                                    lookup_expr="icontains")
    last_name = filters.CharFilter(label=_("Last Name"),
                                   lookup_expr="icontains")
    email = filters.CharFilter(label=_("Email"), lookup_expr="icontains")

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "is_staff", "is_active")


class CityFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("City"), lookup_expr="icontains")

    class Meta:
        model = City
        fields = ("name", "country")


class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Country"), lookup_expr="icontains")

    class Meta:
        model = Country
        fields = ("name",)


class AddressFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Address"), lookup_expr="icontains")

    class Meta:
        model = Address
        fields = (
            "name", "full_name", "phone", "district", "zipcode", "customer",
            "city",)
