from django.db import models
from django.utils.translation import gettext_lazy as _

from core.validators import iban_regex, phone_regex


class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=_("Modified at"), auto_now=True)

    class Meta:
        abstract = True

class AddressAbstractModel(BaseAbstractModel):
    full_name = models.CharField(
        "Full Name",
        max_length=255,
    )
    line_1 = models.CharField(
        "Address Line 1",
        max_length=255,
    )
    line_2 = models.CharField(
        "Address Line 2",
        max_length=255,
    )
    phone = models.CharField(
        "Phone Number",
        max_length=16,
        validators=[phone_regex]
    )
    district = models.CharField(
        "District",
        max_length=255,
    )
    postcode = models.CharField(
        "Post Code",
        max_length=10,
    )
    city = models.ForeignKey(
        "core.City",
        verbose_name=_("City"),
        on_delete=models.PROTECT
    )

    class Meta:
        abstract = True


class Country(BaseAbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Country Name")
    )

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return f"{self.name}"


class City(BaseAbstractModel):
    country = models.ForeignKey(
        "core.Country",
        verbose_name=_("Country"),
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("City Name")
    )

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return f"{self.country} - {self.name}"


class BankAccountAbstractModel(BaseAbstractModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Bank Account Name")
    )
    iban = models.CharField(
        max_length=30,
        verbose_name=_("IBAN Number"),
        validators=[iban_regex]
    )

    class Meta:
        abstract = True
