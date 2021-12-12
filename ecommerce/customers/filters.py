from django_filters import rest_framework as filters

from customers.models import City, Country, Customer, get_all_customer_attrs, Address, get_all_address_attrs


class CityFilter(filters.FilterSet):
    class Meta:
        model = City
        fields = ("name", "country")


class CountryFilter(filters.FilterSet):
    class Meta:
        model = Country
        fields = ("name",)


class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = get_all_customer_attrs()


class AddressFilter(filters.FilterSet):
    class Meta:
        model = Address
        fields = get_all_address_attrs()
