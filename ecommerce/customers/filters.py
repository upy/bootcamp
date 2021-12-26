from django_filters import rest_framework as filters

from customers.models import Address, City, Country, Customer


class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "is_active")


class AddressFilter(filters.FilterSet):
    class Meta:
        model = Address
        fields = ("customer", "name", "city")


class CityFilter(filters.FilterSet):
    class Meta:
        model = City
        fields = ("name", "country")


class CountryFilter(filters.FilterSet):
    class Meta:
        model = Country
        fields = ("name",)
