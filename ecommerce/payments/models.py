from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from localflavor.generic.models import IBANField

from customers.models import Customer


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return str(self.name)


class BankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    bank = models.ForeignKey(Bank, verbose_name=_("Bank"), on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.PROTECT)
    iban = IBANField()

    class Meta:
        verbose_name = _("bank account ")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return f'{self.name} - {self.customer} - {self.bank}'
