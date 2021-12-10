from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from payments.filters import BankFilter, BankAccountFilter
from payments.models import Bank, BankAccount
from payments.serializers import BankSerializer, BankAccountSerializer, BankAccountDetailedSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter


class BankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filterset_class = BankAccountFilter
    serializer_action_classes = {
        "detailed_list": BankAccountDetailedSerializer,
        "detailed": BankAccountDetailedSerializer, }
