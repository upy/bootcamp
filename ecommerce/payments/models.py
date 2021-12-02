from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Bank"))
    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")
    def __str__(self):
        return f"{self.name}"

class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_("Name"), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_("name"))
    iban= models.IntegerField()

    class Meta:
        verbose_name = _("bankaccount")
        verbose_name_plural = _("bankaccounts")
    def __str__(self):
        return f"{self.bank - self.name - self.iban}"