from django.db import models

from core.models import BankAccountAbstractModel, BaseAbstractModel
from django.utils.translation import gettext_lazy as _


class Bank(BaseAbstractModel):
    name = models.CharField(
        verbose_name=_("Bank Name"),
        max_length=255
    )

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return f"{self.name}"


class BankAccount(BankAccountAbstractModel):
    bank = models.ForeignKey(
        "payments.Bank",
        verbose_name=_("Bank"),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"