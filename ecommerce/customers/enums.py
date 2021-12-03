from django.db import models
from django.utils.translation import gettext_lazy as _


class Titles(models.TextChoices):
    HOME = "home", _("Home")
    WORK = "work", _("Work")
    OTHER = "other", _("Other")