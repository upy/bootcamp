from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from core.models import BaseAbstractModel


class Bank(BaseAbstractModel):
    name = models.CharField(unique=True, max_length=511, verbose_name=_("Name"))

    class Meta:
        ordering = ["name"]
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return self.name


class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_("Bank"), on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    # create a regex validator to ensure that the iban is in a valid format
    # 2 letter country code, 2 check digits, up to 30 alphanumeric characters
    iban_regex_validator = RegexValidator(
        regex="/^(?:(?:IT|SM)\d{2}[A-Z]\d{22}|CY\d{2}[A-Z]\d{23}|NL\d{2}[A-Z]{4}\d{10}|LV\d{2}[A-Z]{4}\d{13}|(?:BG|BH|GB|IE)\d{2}[A-Z]{4}\d{14}|GI\d{2}[A-Z]{4}\d{15}|RO\d{2}[A-Z]{4}\d{16}|KW\d{2}[A-Z]{4}\d{22}|MT\d{2}[A-Z]{4}\d{23}|NO\d{13}|(?:DK|FI|GL|FO)\d{16}|MK\d{17}|(?:AT|EE|KZ|LU|XK)\d{18}|(?:BA|HR|LI|CH|CR)\d{19}|(?:GE|DE|LT|ME|RS)\d{20}|IL\d{21}|(?:AD|CZ|ES|MD|SA)\d{22}|PT\d{23}|(?:BE|IS)\d{24}|(?:FR|MR|MC)\d{25}|(?:AL|DO|LB|PL)\d{26}|(?:AZ|HU)\d{27}|(?:GR|MU)\d{28})$/i",
        message=_("Enter your IBAN (without spaces) in the appropriate format.")
    )
    iban = models.CharField(validators=[iban_regex_validator], max_length=34, verbose_name=_("IBAN"))

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return self.iban
