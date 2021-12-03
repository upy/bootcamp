from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from core.models import BaseAbstractModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models

from customers.managers import CustomerManager
from . import enums


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
    """Model for countries"""
    name = models.CharField(max_length=45, verbose_name=_('Country'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'


class City(BaseAbstractModel):
    """Model for cities"""
    name = models.CharField(max_length=55, verbose_name=_('City'))
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Address(BaseAbstractModel):
    title = models.CharField(max_length=20, choices=enums.Titles.choices, verbose_name=_('Address Title'))
    full_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    line1 = models.CharField(max_length=200, verbose_name=_('Address Line1'))
    line2 = models.CharField(max_length=200, blank=True, verbose_name=_('Address Line2'))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    # we can send a verification or information sms to user phone
    # thus, validating phone number is beneficial in this case
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    verbose_name=_('Phone Number'))  # validators should be a list
    district = models.CharField(verbose_name=_('District'), max_length=40,
                                blank=True)
    # A postal code is a series of letters or digits or both, sometimes including spaces or
    # punctuation, included in a postal address for the purpose of sorting mail.
    # due to the above information, taken from wikipedia, used CharField and 12 length
    postal_code = models.CharField(verbose_name=_('Postal Code'), max_length=12)
    city = models.ForeignKey(City, verbose_name=_('City'), on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s, %s' % (self.title, self.city, self.district)

    class Meta:
        verbose_name_plural = 'Addresses'
        unique_together = ('line1', 'line2', 'postal_code', 'city', 'district',)