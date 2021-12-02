from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseAbstractModel


class Bank(BaseAbstractModel):
    """
    Stores bank name, related to :model:payments.BankAccount
    """
    name = models.CharField(max_length=50,
                            verbose_name=_("Bank"))

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return f"{self.name}"


class BankAccount(BaseAbstractModel):
    """
    Stores individual accounts, related to :model:`payments.Bank`
    """
    bank = models.ForeignKey(Bank,
                             on_delete=models.PROTECT)
    name = models.CharField(max_length=50,
                            verbose_name=_("Bank Account"))
    # IBAN field should be changed in a more secure version before deployment
    iban = models.CharField(max_length=50,
                            verbose_name=_("IBAN"))

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return f"{self.bank} : {self.name} : {self.iban}"
