from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from customers.models import City, Country, Customer, Address


class CustomerFilter(filters.FilterSet):
    first_name = filters.CharFilter(label=_("First Name"), lookup_expr="icontains")
    last_name = filters.CharFilter(label=_("Last Name"), lookup_expr="icontains")
    email = filters.CharFilter(label=_("Email"), lookup_expr="icontains")

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Country Name"), lookup_expr="icontains")

    class Meta:
        model = Country
        fields = ("name",)


class CityFilter(filters.FilterSet):
    country = CountryFilter
    name = filters.CharFilter(label=_("City Name"), lookup_expr="icontains")

    class Meta:
        model = City
        fields = ("name", "country")


class AddressFilter(filters.FilterSet):
    customer = CustomerFilter
    name = filters.CharFilter(label=_("Address Name"), lookup_expr="icontains")
    city = CityFilter

    class Meta:
        model = Address
        fields = ("customer", "name", "city")
