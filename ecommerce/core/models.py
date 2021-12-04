from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=_("Modified at"), auto_now=True)

    class Meta:
        abstract = True


class AddressAbstractModel(models.Model):
    """
    Models that are using AddressAbstractModel:\n
    customers.models.Address\n
    orders.models.BillingAddress\n
    orders.models.ShippingAddress\n
    """
    full_name = models.CharField(_("address full name"), max_length=300, blank=True)
    line1 = models.CharField(_("address line one"), max_length=300)
    line2 = models.CharField(_("address line two"), max_length=300, blank=True)
    phone = models.CharField(_("phone number"), max_length=300, blank=True)
    district = models.CharField(_("district"), max_length=300)
    post_code = models.CharField(_("post code"), max_length=50)

    class Meta:
        abstract = True


class BankAccountAbstractModel(models.Model):
    """
    BankAccountAbstractModel for payments\n
    Required Fields: bank, name, iban\n
    Optional Fields: none\n
    One to many relation with Bank
    """
    name = models.CharField(max_length=255, verbose_name=_("Bank Account Name"))
    iban = models.CharField(max_length=26, verbose_name=_("iban"))

    class Meta:
        abstract = True


