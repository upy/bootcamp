from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    OPEN = "open", _("open")
    SUBMITTED = "submitted", _("submitted")
    MERGED = "merged", _("merged")
