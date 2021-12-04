from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseAbstractModel
from django.core.validators import RegexValidator

iban_validator = RegexValidator(regex=r'^[A-Z]{2}[0-9]{2}[A-Z0-9]{4}[0-9]{7}([A-Z0-9]?){0,16}$', message=_('Enter a valid IBAN number.'))


# Model for bank
class Bank(BaseAbstractModel):
    name = models.CharField(max_length=80, verbose_name=_("Bank"))

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return f"{self.name}"


# Model for Bank Account
class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name=_("Bank Account"))
    iban = models.CharField(max_length=50, verbose_name=_("IBAN"), validators=[iban_validator])

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"
