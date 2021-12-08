from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from core.models import BaseAbstractModel

from django.db import models

from customers.managers import CustomerManager


class Country(BaseAbstractModel):
    name = models.CharField(max_length=127, verbose_name=("name"))

    def __str__(self):
        return f"{self.name}"


class City(BaseAbstractModel):
    country = models.ForeignKey(Country,verbose_name=("Country"),
                               on_delete=models.PROTECT)
    name = models.CharField(max_length=127, verbose_name=("name"))

    def __str__(self):
        return f"{self.country} - {self.name}"


class Address(BaseAbstractModel):

    city = models.ForeignKey(City,verbose_name=("City"),
                             on_delete=models.PROTECT)

    name = models.CharField(max_length=127, verbose_name=("name"))
    fullname = models.CharField(max_length=255, verbose_name=("fullname"))
    address1 = models.CharField(max_length=1024, verbose_name=("Address line 1"))
    address2 = models.CharField(max_length=1024, verbose_name=("Address line 2"))
    phone_validator = RegexValidator(regex=r'^[0-9]+$',
                                 message="Phone number must be entered as all numeric"
                                         "in the format 05555555555"
                                         "up to 16 digits")

    phone = models.CharField(validators=[phone_validator], max_length=16, verbose_name="phone")

    district = models.CharField(max_length=127, verbose_name=("district"))

    postcode_validator = RegexValidator(regex=r'^[0-9]+$',
                                 message="Postcode must be entered as all numeric "
                                         "up to 10 digits 0123456789" )
    postcode = models.CharField(validators=[postcode_validator], max_length=10, verbose_name="postcode")


    def __str__(self):
        return f"{self.fullname} - {self.city}"




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

