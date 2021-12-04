from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _

"""
Using the max and min possible for country phone numbers while separating
the country code to easily split.
"""
phone_regex = RegexValidator(
    regex=r'/^(05)([0-9]{2})\s?([0-9]{3})\s?([0-9]{2})\s?([0-9]{2})$/',
    message=_("You have entered an invalid phone number. Please try again. Example: '05231231212', '0523 123 12 12'")
)

iban_regex = RegexValidator(
    regex=r'\b[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?!(?:[ ]?[0-9]){3})(?:[ ]?[0-9]{1,2})?\b',
    message=_("You have entered an IBAN") # https://regex101.com/r/dzDqmM/54
)
