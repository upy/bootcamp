from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseAbstractModel
from django_iban.fields import IBANField, SWIFTBICField


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('bank')
        verbose_name_plural = _('banks')

    def __str__(self):
        return f'{self.name}'


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_('Bank'),
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    iban = IBANField()

    class Meta:
        verbose_name = _('Bank Accounts')
        verbose_name_plural = _('Bank Accounts')

    def __str__(self):
        return f'{self.bank} - {self.name}'

# Create your models here.
