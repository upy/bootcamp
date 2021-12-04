from django.db import models
from customers.models import Customer
from baskets import enums
from products.models import Product
from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.


class Bank(BaseAbstractModel):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")
    def __str__(self):
        return f"{self.name}"

class BankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=("Bank"),
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=False)
    iban_validator = RegexValidator(regex=r'^[A-Za-z0-9]+$',
                                 message="iban must be an alphanumeric value "
                                         "34 characters at most" )
    iban = models.CharField(validators=[iban_validator], max_length=34, verbose_name="iban")


    def __str__(self):
        return f"{self.bank} - {self.name}"

