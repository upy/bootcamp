from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission


class PhoneNumberValidator(RegexValidator):
    """
    Validator for phone numbers.
    """
    regex = r'^\+[0-9]{1,3}\d{10}$'
    message = _(
        'Phone number must be entered in the format: +901234567890. '
        'Up to 13 digits allowed.'
    )
    flags = 0


class IBANValidator(RegexValidator):
    """
    Validator for IBAN numbers.
    """
    regex = r'^[A-Z]{2}[0-9]{2}[A-Z0-9]{4}[0-9]{7}([A-Z0-9]?){0,16}$'
    message = _('Enter a valid IBAN number.')
    flags = 0


phonenumber_validator = PhoneNumberValidator()
iban_validator = IBANValidator()


class IsStaffUserAuthenticated(BasePermission):
    # check is current authenticated user (if exists) staff or not
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class IsLoggedIn(BasePermission):
    # check whether user has logged in
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class CanCreateUser(BasePermission):
    # two types of users can create accounts:
    # guest (not logged in) user
    # staff user
    def has_permission(self, request, view):
        return IsStaffUserAuthenticated.has_permission(self, request, view) \
            or not (IsLoggedIn.has_permission(self, request, view))
