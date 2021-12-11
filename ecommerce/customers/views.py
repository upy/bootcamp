from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from customers.filters import CustomerFilter, CityFilter, CountryFilter, AddressFilter
from customers.models import Country, City, Customer, Address
from customers.serializers import CountrySerializer, CitySerializer, CityDetailedSerializer, \
    CustomerSerializer, AddressSerializer, AddressDetailedSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    filterset_class = CountryFilter
    serializer_class = CountrySerializer


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer,
    }


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    filterset_class = CustomerFilter
    serializer_class = CustomerSerializer


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }

