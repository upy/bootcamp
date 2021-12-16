from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet

from core.mixins import DetailedViewSetMixin
from core.utils import IsStaffUserAuthenticated
from customers.filters import CustomerFilter, AddressFilter, CountryFilter, CityFilter
from customers.models import Customer, Address, City, Country
from customers.serializers import CustomerSerializer, AddressSerializer, CitySerializer, \
    CountrySerializer, \
    AddressDetailedSerializer, CityDetailedSerializer, ProfileSerializer, RegisterSerializer


class AdminCustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
        IsStaffUserAuthenticated
    )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter


class MyProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {"id": self.request.user.id}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = ()
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer,
    }


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)


class RegisterViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    Register new customer endpoint
    """
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = ()
    http_method_names = ["get", "put"]

    def get_object(self):
        """
        Each customer must see own profile
        :return: Customer Object
        """
        queryset = self.get_queryset()
        filter_kwargs = {"id": self.request.user.id}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj

