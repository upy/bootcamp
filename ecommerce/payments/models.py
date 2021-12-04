from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=50, verbose_name=_("Bank"))

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return f"{self.name}"


class BankAccounts(BaseAbstractModel):
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    iban = models.CharField(max_length=50, verbose_name="IBAN", null=False)

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"
# Create your models here.
