from django.db import models
from django.utils.translation import gettext_lazy as _
from .regex_validators import PHONE_REGEX, POSTCODE_REGEX


class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=_("Modified at"), auto_now=True)

    class Meta:
        abstract = True


class Country(BaseAbstractModel):
    """Model for countries"""
    name = models.CharField(max_length=45, verbose_name=_('Country'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'


class City(BaseAbstractModel):
    """Model for cities"""
    name = models.CharField(max_length=55, verbose_name=_('City'))
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class BaseAbstractAddressModel(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    line1 = models.CharField(max_length=200, verbose_name=_('Address Line1'))
    line2 = models.CharField(max_length=200, blank=True, verbose_name=_('Address Line2'))
    # we can send a verification or information sms to user phone
    # thus, validating phone number is beneficial in this case
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=15, blank=True,
                                    verbose_name=_('Phone Number'))  # validators should be a list
    district = models.CharField(verbose_name=_('District'), max_length=40,
                                blank=True)
    # A postal code is a series of letters or digits or both, sometimes including spaces or
    # punctuation, included in a postal address for the purpose of sorting mail.
    # due to the above information, taken from wikipedia, used CharField and 12 length
    postal_code = models.CharField(validators=[POSTCODE_REGEX], verbose_name=_('Postal Code'), max_length=12)
    city = models.ForeignKey(City, verbose_name=_('City'), on_delete=models.PROTECT)

    class Meta:
        abstract = True
