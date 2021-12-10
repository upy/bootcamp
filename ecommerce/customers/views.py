from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from customers.filters import CityFilter, CountryFilter, CustomerFilter, AddressFilter
from customers.models import City, Country, Customer, Address
from customers.serializers import CustomerSerializer, CitySerializer, CountrySerializer, AddressSerializer, \
    CityDetailedSerializer, AddressDetailedSerializer


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer,
    }


class CountryViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter


class CustomerViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }