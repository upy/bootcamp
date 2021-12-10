from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
# from products.filters import ProductFilter
from customers.models import Customer
from customers.serializers import *


class CustomerViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # filterset_class = ProductFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressDetailedSerializer
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }
