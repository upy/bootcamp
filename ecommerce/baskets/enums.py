from django.db import models
from django.utils.translation import gettext_lazy as _


class Statuses(models.TextChoices):
    OPEN = "open", _("Open")
    SUBMITTED = "submitted", _("Submitted")
    MERGED = "merged", _("Merged")
