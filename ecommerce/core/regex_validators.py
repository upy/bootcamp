"""Regex Validator Collection

This file contains regex validators used in this project. The file should be
kept up to date as new regular expression validators are created.
"""

from django.core.validators import RegexValidator


IBAN_REGEX = RegexValidator(regex='^(?:(?:IT|SM)\d{2}[A-Z]\d{22}|CY\d{2}[A-Z]\d{23}|NL\d{2}[A-Z]{4}\d{10}|LV\d{2}[A-Z]{4}\d{13}|(?:BG|BH|GB|IE)\d{2}[A-Z]{4}\d{14}|GI\d{2}[A-Z]{4}\d{15}|RO\d{2}[A-Z]{4}\d{16}|KW\d{2}[A-Z]{4}\d{22}|MT\d{2}[A-Z]{4}\d{23}|NO\d{13}|(?:DK|FI|GL|FO)\d{16}|MK\d{17}|(?:AT|EE|KZ|LU|XK)\d{18}|(?:BA|HR|LI|CH|CR)\d{19}|(?:GE|DE|LT|ME|RS)\d{20}|IL\d{21}|(?:AD|CZ|ES|MD|SA)\d{22}|PT\d{23}|(?:BE|IS)\d{24}|(?:FR|MR|MC)\d{25}|(?:AL|DO|LB|PL)\d{26}|(?:AZ|HU)\d{27}|(?:GR|MU)\d{28})$', message="Please enter correct IBAN sequence")

PHONE_REGEX = RegexValidator(regex=r'^[0-9]+$', message=("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))

POSTCODE_REGEX = RegexValidator(regex=r'^[0-9]+$', message=("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))


# Depending on the design choice, validators can be created in models.py files
# In that case, this file should hold only regexes and messages
patterns = {
    "IBAN_REG": {'message': "Please enter correct IBAN sequence", 'regex':'/^(?:(?:IT|SM)\d{2}[A-Z]\d{22}|CY\d{2}[A-Z]\d{23}|NL\d{2}[A-Z]{4}\d{10}|LV\d{2}[A-Z]{4}\d{13}|(?:BG|BH|GB|IE)\d{2}[A-Z]{4}\d{14}|GI\d{2}[A-Z]{4}\d{15}|RO\d{2}[A-Z]{4}\d{16}|KW\d{2}[A-Z]{4}\d{22}|MT\d{2}[A-Z]{4}\d{23}|NO\d{13}|(?:DK|FI|GL|FO)\d{16}|MK\d{17}|(?:AT|EE|KZ|LU|XK)\d{18}|(?:BA|HR|LI|CH|CR)\d{19}|(?:GE|DE|LT|ME|RS)\d{20}|IL\d{21}|(?:AD|CZ|ES|MD|SA)\d{22}|PT\d{23}|(?:BE|IS)\d{24}|(?:FR|MR|MC)\d{25}|(?:AL|DO|LB|PL)\d{26}|(?:AZ|HU)\d{27}|(?:GR|MU)\d{28})$/i', },
    "PHONE_REG": {'message':"Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", 'regex':'^[0-9]+$'},
    "POSTCODE_REG": {'message':"Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed.",'regex':'^[0-9]+$'},
            }
