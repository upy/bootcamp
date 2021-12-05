from django.db import models
from django.utils.translation import gettext_lazy as _


##Used for creating choices for basket.status.

class BasketStatus(models.TextChoices):
    OPEN = "Open", _("Open")
    SUBMITTED = "Submitted", _("Submitted")
    MERGED = "Merged", _("Merged")

