from django.db import models
from django.utils.translation import gettext_lazy as _


class BasketStatus(models.TextChoices):
    """
    Basket status choices.
    """
    OPEN = "open", _("Open")
    SUBMITTED = "submitted", _("Submitted")
    MERGED = "merged", _("Merged")
