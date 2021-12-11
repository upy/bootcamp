from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from customers.filters import CustomerFilter, CityFilter, CountryFilter, \
    AddressFilter
from customers.models import Customer, City, Country, Address
from customers.serializers import CustomerSerializer, \
    AddressDetailedSerializer, CountrySerializer, CitySerializer, \
    CityDetailedSerializer, AddressSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = City.objects.select_related("country").all()
    serializer_class = CitySerializer
    filterset_class = CityFilter
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detail": CityDetailedSerializer,
    }


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detail": AddressDetailedSerializer,
    }
