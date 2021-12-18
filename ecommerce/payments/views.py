from rest_framework import permissions, viewsets

from core.mixins import DetailedViewSetMixin
from payments.filters import BankAccountFilter, BankFilter
from payments.models import BankAccount, Bank
from payments.serializers import BankAccountSerializer, BankSerializer, BankAccountDetailedSerializer


class BankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filterset_class = BankAccountFilter
    serializer_action_classes = {
        "detailed_list": BankAccountDetailedSerializer,
        "detailed": BankAccountDetailedSerializer,
    }


class BankViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter

