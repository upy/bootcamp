from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from core.mixins import DetailedViewSetMixin
from payments.filters import BankFilter, BankAccountFilter
from payments.models import Bank, BankAccount
from payments.serializer import BankSerializer, BankAccountSerializer, BankAccountDetailedSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter


class BankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BankAccount.object.all()
    serializer_class = BankAccountSerializer
    filterset_class = BankAccountFilter
    serializer_action_classes = {
        "detailed_list": BankAccountDetailedSerializer,
        "detailed": BankAccountDetailedSerializer,
    }
