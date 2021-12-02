from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models

from core.models import BaseAbstractModel
from customers.managers import CustomerManager


class Customer(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(
        _("email address"), unique=True, validators=[username_validator]
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Country(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name


class City(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100, unique=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name="country"
    )

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return self.name


class Address(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100, unique=True)
    full_name = models.CharField(verbose_name=_("Full Name"), max_length=100)
    line1 = models.TextField(verbose_name=_("Line1"))
    line2 = models.TextField(verbose_name=_("Line2"))
    phone_regex = RegexValidator(regex=r'^\+(\d{2})\s\((\d{3})\)\s(\d{3})\s(\d{2})\s(\d{2})',
                                 message="Phone number must be entered in the format: '+99 (999) 999 99 99'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=19)
    district = models.CharField(verbose_name=_("District"), max_length=100)
    post_code = RegexValidator(regex=r'\d{5}',
                               message="postcode must be entered in the format: '99999'.")
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name="city"
    )

    class Meta:
        abstract = True