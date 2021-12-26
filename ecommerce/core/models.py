from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseAbstractModel(models.Model):
    """
    Abstract model to be inherited by all models.
    """

    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=_("Modified at"), auto_now=True)

    class Meta:
        abstract = True
