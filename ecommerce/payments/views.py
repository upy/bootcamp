from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from payments.filters import BankAccountFilter, BankFilter
from payments.models import BankAccount, Bank
from payments.serializers import BankAccountSerializer, BankSerializer, BankAccountDetailedSerializer


class BankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filterset_class = BankAccountFilter
    serializer_action_classes = {
        "detailed_list": BankAccountDetailedSerializer,
        "detailed": BankAccountDetailedSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)


class BankViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter

