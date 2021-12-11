
from django_filters import rest_framework as filters
from customers.models import Customer, Address




class CustomerFilter(filters.FilterSet):

    class Meta:
        model = Customer
        fields = ("is_active", "is_staff")

class AddressFilter(filters.FilterSet):

    class Meta:
        model = Address
        fields = ("name", "city")