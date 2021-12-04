from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from core.utils import IBANValidator


class Bank(BaseAbstractModel):
    """
    Bank model
    """
    name = models.CharField(max_length=100, verbose_name=_("Bank Name"))

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return self.name


class BankAccount(BaseAbstractModel):
    """
    Bank Account model
    """
    iban_validator = IBANValidator()
    bank = models.ForeignKey(Bank, verbose_name=_("Bank Name"), on_delete=models.PROTECT)
    name = models.CharField(max_length=100, verbose_name=_("Bank Account Name"))
    iban = models.CharField(max_length=100, verbose_name=_("IBAN"), validators=[iban_validator])

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")
    
    def __str__(self):
        return f"{self.name} - {self.iban}"
