from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    """
    returns: none
    superclass: models.TextChoices
    This class has choices of the status of the basket class
    """
    OPEN = "open", _("Open")
    SUBMITTED = "submitted", _("Submitted")
    MERGED = "merged", _("Merged")

