from django.db import models
from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _


class Bank(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    name = models.CharField(verbose_name=_("name"), max_length=75)

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return  self.name


class BankAccount(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    name = models.CharField(verbose_name=_("name"), max_length=75)
    iban = models.CharField(max_length=34)

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return f"{self.bank} - {self.name}"
