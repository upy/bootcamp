from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from .managers import CustomerManager
from django.core.validators import RegexValidator  # Import forms library to use forms.RegexField for Address.phone/postcode


class Country(AbstractBaseUser):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    name = models.CharField(verbose_name=_("name"), max_length=56)

    def __srt__(self):
        return self.name


class City(AbstractBaseUser):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    name = models.CharField(verbose_name=_("name"), max_length=35)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.country}"


class Address(AbstractBaseUser):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class, forms.ModelForm Class
    """
    name = models.CharField(verbose_name=_("name"), max_length=100)
    full_name = models.CharField(verbose_name=_("full name"), max_length=200)
    line1 = models.CharField(verbose_name=_("line1"), max_length=250)
    line2 = models.CharField(verbose_name=_("line2"), max_length=250)
    phone_regex = RegexValidator(regex=r'^[0-9]+$',
                                 message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits "
                                         "allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, verbose_name='phone', null=True)
    district = models.CharField(verbose_name=_("district"), max_length=100)
    postcode_regex = RegexValidator(regex=r'^[0-9]+$', message=("Postal Code must be entered in the format: "
                                                                "'1234567'. Up to 7 digits allowed."))
    postcode = models.CharField(validators=[postcode_regex], max_length=7, verbose_name='Postal code')
    city = models.ForeignKey(City, on_delete=models.PROTECT)


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
    addresses = models.ManyToManyField(Address)
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
