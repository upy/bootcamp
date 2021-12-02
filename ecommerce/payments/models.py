from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel


class Bank(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")


class BankAccount(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100, unique=True)
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        verbose_name="bank"
    )
    iban = RegexValidator(regex=r'\b[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?!(?:[ ]?[0-9]){3})(?:[ ]?[0-9]{1,2})?\b',
                               message="iban must be entered in the format: '9999999999999999999999'\n or in the "
                                       "format: '9999 9999 9999 9999 9999 99'.")

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")

