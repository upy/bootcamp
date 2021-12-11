from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import ugettext_lazy as _

from customers.models import City, Country, Customer, Address


class CityFilter(filters.FilterSet):
    name = filters.CharFilter(label=_('Name'), method='filter_name')

    class Meta:
        model = City
        fields = ("name", "country")
    
    def filter_name(self, qs, name, value):
        return qs.filter(Q(name__icontains=value))


class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(label=_('Name'), method='filter_name')

    class Meta:
        model = Country
        fields = ("name",)
    
    def filter_name(self, qs, name, value):
        return qs.filter(Q(name__icontains=value))


class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")


class AddressFilter(filters.FilterSet):
    class Meta:
        model = Address
        fields = ("customer", "name", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")