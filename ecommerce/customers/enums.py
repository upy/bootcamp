from django.db import models
from django.utils.translation import ugettext as _


class AddressTypeEnum(models.TextChoices):
    BILLING = "BI", _("Billing")
    SHIPPING = "SH", _("Shipping")
    BILLING_SHIPPING = "BS", _("Billing & Shipping")
