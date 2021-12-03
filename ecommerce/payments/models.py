from django.db import models
from django.utils.translation import gettext_lazy as _


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


class BankAccount(models.Model):
    """
    BankAccount model for payments\n
    Required Fields: bank, name, iban\n
    Optional Fields: none\n
    One to many relation with Bank
    """
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, verbose_name=_("Bank Account Name"))
    iban = models.CharField(max_length=26, verbose_name=_("iban"))

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("banks accounts")

    def __str__(self):
        return f"{self.name}-{self.bank}"
