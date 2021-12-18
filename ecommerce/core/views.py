from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from core.serializers import APITokenObtainPairSerializer, RegisterCustomerSerializer
from customers.models import Customer


class APITokenObtainPairView(TokenObtainPairView):
    serializer_class = APITokenObtainPairSerializer


class RegisterCustomerView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterCustomerSerializer