from rest_framework import viewsets
from core.mixins import DetailedViewSetMixin


from customers.filters import CustomerFilter, AddressFilter
from customers.models import Customer, Address, City, Country
from customers.serializers import CustomerSerializer, AddressSerializer, CitySerializer, CountrySerializer, \
        AddressDetailedSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter

class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter

class AddressDetailedViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressDetailedSerializer
    http_method_names = ["get"]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
