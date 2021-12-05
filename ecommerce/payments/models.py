from django.db import models
from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return f"{self.name}"


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    iban = models.PositiveIntegerField(verbose_name=_("IBAN"))

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return f"{self.bank} - {self.name}"