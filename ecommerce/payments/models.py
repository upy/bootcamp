from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel


class Bank(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Bank name"),
                            max_length=255)

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return f"{self.name}"


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank,
                             verbose_name=_("Bank"),
                             on_delete=models.CASCADE,
                             null=False
                             )
    name = models.CharField(verbose_name=_("Bank account name"),
                            max_length=255
                            )
    iban = models.CharField(verbose_name=_("IBAN number"),
                            max_length=30,
                            null=False
                            )

    class Meta:
        verbose_name =_("bank account")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"
