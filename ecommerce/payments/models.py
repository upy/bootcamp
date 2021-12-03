from django.db import models
from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

IBAN_REGEX = "^[a-zA-Z]{2}[0-9]{2}\s?[a-zA-Z0-9]{4}\s?[0-9]{4}\s?[0-9]{3}([a-zA-Z0-9]\s?[a-zA-Z0-9]{0,4}\s?[a-zA-Z0-9]{0,4}\s?[a-zA-Z0-9]{0,4}\s?[a-zA-Z0-9]{0,3})?$"


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('bank')
        verbose_name_plural = _('banks')

    def __str__(self):
        return f'{self.name}'


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_('Bank'), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    iban_regex = RegexValidator(regex=IBAN_REGEX, message="Your IBAN number is invalid.")
    iban = models.CharField(validators=[iban_regex], max_length=34, verbose_name=_('IBAN'), unique=True)

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return f"{self.bank} - {self.name}"
