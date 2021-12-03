from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from django.db import models

from core.models import BaseAbstractModel
from customers.managers import CustomerManager

phone_regex = RegexValidator(regex=r'^\+?1?\d{20}$',
                             message="Phone number must be entered in the format: '+999999999'. '+' sign and 19 digits")


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

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"



    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    def __str__(self):
        return f"{self.name} - {self.line1} - {self.line2} - {self.city}"


class Country(BaseAbstractModel):
    name = models.CharField(_("Country name"),
                            max_length=255)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return f"{self.name}"


class City(BaseAbstractModel):
    name = models.CharField(_("City name"),
                            max_length=255)
    country = models.ForeignKey(Country,
                                verbose_name=_("Country"),
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return f"{self.name} - {self.country}"


class Address(BaseAbstractModel):
    name = models.CharField(verbose_name=_("name"),
                            max_length=50
                            )
    full_name = models.CharField(verbose_name=_("Full name"),
                                 max_length=100
                                 )
    line1 = models.CharField(verbose_name=_("Line 1"),
                             max_length=255
                             )
    line2 = models.CharField(verbose_name=_("Line 2"),
                             max_length=255
                             )
    phone = models.CharField(validators=[phone_regex],
                             max_length=20
                             )
    district = models.CharField(verbose_name=_("District"),
                                max_length=255
                                )
    postcode = models.CharField(verbose_name=_("Post code"),
                                max_length=20)

    # since we would like to keep city information,
    # we put PROTECT on_delete over city which could be deleted by mistake
    city = models.ForeignKey(City,
                             verbose_name=_("City"),
                             on_delete=models.PROTECT)
