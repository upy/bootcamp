from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=_("Modified at"), auto_now=True)

    class Meta:
        abstract = True

class Country(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Country Name"))

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return f"{self.name}"


class City(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("City Name"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return f"{self.name}"

class BaseAbstractAddressModel(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line1 = models.CharField(max_length=255, verbose_name=_("Line 1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Line 2"))

    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                           message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=255, verbose_name=_("Phone"), validators=[phone_validator])

    district = models.CharField(max_length=255, verbose_name=_("District"))

    postal_code_validator = RegexValidator(regex=r'(?i)^[a-z0-9][a-z0-9\- ]{0,10}[a-z0-9]$',
                                 message="Invalid format.")  # https://stackoverflow.com/a/19844362/12579069
    postal_code = models.CharField(max_length=255, verbose_name=_("Postal Code"), validators=[postal_code_validator])

    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        abstract = True