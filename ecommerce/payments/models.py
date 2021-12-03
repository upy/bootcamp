from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BankAccountAbstractModel

class Bank(models.Model):
    """
    Bank model for payments\n
    Required Fields: name\n
    Optional Fields: none\n
    """
    name = models.CharField(max_length=255, verbose_name=_("Bank Name"))

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return self.name


class BankAccount(BankAccountAbstractModel):
    """
    BankAccount model for payments\n
    Required Fields: bank, name, iban\n
    Optional Fields: none\n
    One to many relation with Bank
    """
    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("banks accounts")

    def __str__(self):
        return f"{self.name}-{self.bank}"
