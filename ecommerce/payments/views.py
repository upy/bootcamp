from rest_framework import viewsets

from payments.models import Bank, BankAccount
from payments.serializers import PaymentSerializer, BankSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = PaymentSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
