from django.utils.translation import gettext_lazy as _

from django_filters import rest_framework as filters
from customers.models import Customer, Address,  Country, City


class CustomerFilter(filters.FilterSet):
    email = filters.CharFilter(label=_("Email"))

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class CityFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("City"))

    class Meta:
        model = City
        fields = ("name", "country")


class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Country"))

    class Meta:
        model = Country
        fields = ("name",)


class AddressFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("Address"))

    class Meta:
        model = Address
        fields = ("name", "full_name", "phone", "district", "zipcode", "city", "customer")

        
