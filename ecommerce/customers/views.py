from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from customers.filters import CustomerFilter, AddressFilter, CityFilter
from customers.models import Customer, Address, City
from customers.serializers import CustomerSerializer, AddressSerializer, AddressDetailedSerializer, \
    CityDetailedSerializer, CitySerializer


class CustomerViewSet(viewsets.ModelViewSet):
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


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer,
    }
