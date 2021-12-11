from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from customers.models import Country, City, Address, Customer
from customers.serializers import CountrySerializer, CitySerializer, AddressSerializer, CustomerSerializer, \
    CityDetailedSerializer, AddressDetailedSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer,
    }


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.non_staff_users()
    serializer_class = CustomerSerializer
