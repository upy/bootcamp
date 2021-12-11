from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from customers.serializers import AddressSerializer, CitySerializer, CountrySerializer, CustomerSerializer
from customers.models import Address, City, Country, Customer
from customers.filters import CityFilter, CountryFilter, CustomerFilter, AddressFilter


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter
    # serializer_action_classes = {
    #     "detailed_list": CityDetailedSerializer,
    #     "detailed": CityDetailedSerializer
    # }


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter
    # serializer_action_classes = {
    #     "detailed_list": CountryDetailedSerializer,
    #     "detailed": CountryDetailedSerializer
    # }


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter
    # serializer_action_classes = {
    #     "detailed_list": CustomerDetailedSerializer,
    #     "detailed": CustomerDetailedSerializer
    # }


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    # serializer_action_classes = {
    #     "detailed_list": AddressDetailedSerializer,
    #     "detailed": AddressDetailedSerializer
    # }
