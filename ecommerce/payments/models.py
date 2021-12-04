from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from core.models import BaseAbstractModel


class Bank(BaseAbstractModel):
    name = models.CharField(unique=True, max_length=511, verbose_name=_("Name"))

    class Meta:
        ordering = ["name"]
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return self.name


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_("Bank"), on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    # create a regex validator to ensure that the iban is in a valid format
    # 2 letter country code, 2 check digits, up to 30 alphanumeric characters
    iban_regex_validator = RegexValidator(
        regex=r"^[A-Z]{2}[a-zA-Z0-9]{10,34}$",
        message=_("Enter your IBAN (without spaces) in the appropriate format.")
    )
    iban = models.CharField(validators=[iban_regex_validator], max_length=34, verbose_name=_("IBAN"))

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return self.iban
