from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from ecommerce.utils import Regex
from ecommerce.utils import ValidatorMessage


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
    iban_regex = RegexValidator(regex=Regex.IBAN,
                                message=ValidatorMessage.IBAN)
    iban = models.CharField(validators=[iban_regex], max_length=27)

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")
