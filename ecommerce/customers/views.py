from django.shortcuts import render
from rest_framework import viewsets
from customers.serializers import CustomerSerializer, CitySerializer, CountrySerializer,\
    AddressSerializer, AddressDetailedSerializer, CityDetailedSerializer
from customers.models import Customer, City, Country, Address
from customers.filters import AddressFilter, CustomerFilter
from core.mixins import DetailedViewSetMixin
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class =  CustomerFilter

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer
    }

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer
    }

