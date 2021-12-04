from django.db import models
from django.utils.translation import gettext_lazy as _


class BasketStatus(models.TextChoices):
    OPEN = "OP", _("Open")
    SUBMITTED = "SB", _("Submitted")
    MERGED = "ME", _("Merged")
