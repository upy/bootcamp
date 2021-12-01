from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS_TYPE_OPEN = 0
STATUS_TYPE_SUBMITTED = 1
STATUS_TYPE_MERGED = 2


class StatusTypes(models.TextChoices):
    OPEN = "open", _("Open")
    SUBMITTED = "submitted", _("Submitted")
    MERGED = "merged", _("Merged")
