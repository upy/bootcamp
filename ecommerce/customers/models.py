from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models

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


class Country(models.Model):
    """
    Country model for address\n
    Required Fields: name\n
    Optional Fields: none\n
    One to many relation with City model
    """
    name = models.CharField(_("country"), max_length=150)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name


class City(models.Model):
    """
    City model for address\n
    Required Fields: name, country\n
    Optional Fields: none\n
    One to many relation with Country and Address models
    """
    name = models.CharField(_("city"), max_length=150)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return self.name


class Address(models.Model):
    """
    Address Model for customer's address\n
    Required Fields: name, line1, district, post_code, city\n
    Optional Fields: full_name, line2, phone\n
    One to many relation with City model.
    """
    name = models.CharField(_("address name"), max_length=150)
    full_name = models.CharField(_("address full name"), max_length=300, blank=True)
    line1 = models.CharField(_("address line one"), max_length=300)
    line2 = models.CharField(_("address line two"), max_length=300, blank=True)
    phone = models.CharField(_("phone number"), max_length=300, blank=True)
    district = models.CharField(_("district"), max_length=300)
    post_code = models.CharField(_("post code"), max_length=50)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    def __str__(self):
        return self.name
