from rest_framework import viewsets
from core.mixins import DetailedViewSetMixin
from core.mixins import DetailedViewSetMixin
from payments.filters import BankAccountFilter
from payments.models import Bank, BankAccount
from payments.serializers import BankSerializer, BankAccountSerializer, BankAccountDetailedSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class BankAccountDetailedViewSet(BankAccountViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountDetailedSerializer
    http_method_names = ["get"]
