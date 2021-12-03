from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from core.models import BaseAbstractModel

IBAN_REGEX = RegexValidator('^[0-9]*$')


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Bank Name"))

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return f"{self.name}"


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_("Bank Name"), on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    iban = models.CharField(max_length=16, validators=[IBAN_REGEX], verbose_name="IBAN")

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"
