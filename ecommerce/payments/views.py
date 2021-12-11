from django.shortcuts import render
from rest_framework import viewsets
from payments.serializers import BankSerializer, BankAccountSerializer,BankAccountDetailedSerializer
from payments.models import Bank, BankAccount
from core.mixins import DetailedViewSetMixin
from payments.filters import BankAccountFilter
# Create your views here.

class BankViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankAccountViewSet(DetailedViewSetMixin,viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filterset_class = BankAccountFilter
    serializer_action_classes = {
        "detailed_list": BankAccountDetailedSerializer,
        "detailed": BankAccountDetailedSerializer
    }

