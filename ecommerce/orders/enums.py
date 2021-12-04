from django.db import models
from django.utils.translation import ugettext as _


class OrderStatusEnum(models.TextChoices):
    PAYMENT_WAITING = "PW", _("Payment Waiting")
    COMPLETED = "CO", _("Completed")
    CANCELED = "CA", _("Canceled")
