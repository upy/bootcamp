from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from customers.models import Customer, Address, City, Country


class CityFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = City
        fields = ("name", "country",)


class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = Country
        fields = ("name",)


class CustomerFilter(filters.FilterSet):
    first_name = filters.CharFilter(label=_("First Name"), lookup_expr="icontains")
    last_name = filters.CharFilter(label=_("Last Name"), lookup_expr="icontains")
    email = filters.CharFilter(label=_("Email"), lookup_expr="icontains")

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class AddressFilter(filters.FilterSet):

    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")
    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    line_1 = filters.CharFilter(label=_("Address Line 1"), lookup_expr="icontains")
    line_2 = filters.CharFilter(label=_("Address Line 2"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")

    class Meta:
        model = Address
        fields = ("customer", "name", "full_name",
                  "line_1", "line_2", "phone", "district", "zipcode", "city", "is_default")
