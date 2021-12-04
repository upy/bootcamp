from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=_("Modified at"), auto_now=True)

    class Meta:
        abstract = True


class AddressAbstractModel(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_one = models.CharField(max_length=511, verbose_name=_("Line One"))
    line_two = models.CharField(max_length=511, verbose_name=_("Line Two"))
    # regex validator that accepts a "+" symbol followed by 9 to 15 digits in accordance with E.164 format
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message=_(
            "Enter phone number in the following format: '+xxxxxxxxxxxx'. Up to 15 digits including country code.")
    )
    phone = models.CharField(validators=[phone_regex], max_length=16, verbose_name=_("Phone Number"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    # regex validator for postal codes. Does not guarantee validity but provides an acceptable boundary
    post_code_regex = RegexValidator(
        regex=r'(?i)^[a-z0-9][a-z0-9\- ]{0,10}[a-z0-9]$',
        message=_("Enter a valid post/zip code")
    )
    post_code = models.CharField(validators=[post_code_regex], max_length=11, null=True, verbose_name=_("Post Code"))

    class Meta:
        abstract = True
