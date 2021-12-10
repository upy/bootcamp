from rest_framework import viewsets
from core.mixins import DetailedViewSetMixin
from customers.models import Country, City, Address, Customer
from customers.serializers import CountrySerializer, CitySerializer, \
    CityDetailedSerializer, CustomerSerializer, AddressSerializer,\
    AddressDetailedSerializer
from customers.managers import CustomerManager


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = City.objects.action_detailed_list()
    serializer_class = CitySerializer
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer,
    }


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.action_detailed_list()
    serializer_class = AddressSerializer
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }