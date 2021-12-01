from django.db import models

from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _


class Bank(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Bank Name"), max_length=255)

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return f"{self.name}"


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_("Bank"),
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_("Bank Account Name"))
    iban = models.CharField(max_length=255, verbose_name=_("IBAN Number"))

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"
