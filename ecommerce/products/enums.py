from django.db import models
from django.utils.translation import gettext_lazy as _


class Colors(models.TextChoices):
    """
    Colors of the product
    """

    RED = "red", _("Red")
    BLUE = "blue", _("Blue")
    WHITE = "white", _("White")
    YELLOW = "yellow", _("Yellow")
