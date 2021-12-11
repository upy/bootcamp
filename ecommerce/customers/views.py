from rest_framework import viewsets
from core.mixins import DetailedViewSetMixin

from customers.models import Address, City, Country, Customer
from customers.serializers import (AddressSerializer, AddressDetailedSerializer,
                                   CitySerializer, CityDetailedSerializer,
                                   CountrySerializer, CustomerSerializer)
from customers.filters import AddressFilter, CityFilter, CountryFilter, CustomerFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(is_active=True)
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter


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


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }
