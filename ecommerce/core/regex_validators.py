from django.core.validators import RegexValidator

IBAN_REGEX = RegexValidator(regex='/^(?:(?:IT|SM)\d{2}[A-Z]\d{22}|CY\d{'
                                  '2}[A-Z]\d{23}|NL\d{2}[A-Z]{4}\d{'
                                  '10}|LV\d{2}[A-Z]{4}\d{13}|('
                                  '?:BG|BH|GB|IE)\d{2}[A-Z]{4}\d{'
                                  '14}|GI\d{2}[A-Z]{4}\d{15}|RO\d{2}['
                                  'A-Z]{4}\d{16}|KW\d{2}[A-Z]{4}\d{'
                                  '22}|MT\d{2}[A-Z]{4}\d{23}|NO\d{13}|('
                                  '?:DK|FI|GL|FO)\d{16}|MK\d{17}|('
                                  '?:AT|EE|KZ|LU|XK)\d{18}|('
                                  '?:BA|HR|LI|CH|CR)\d{19}|('
                                  '?:GE|DE|LT|ME|RS)\d{20}|IL\d{21}|('
                                  '?:AD|CZ|ES|MD|SA)\d{22}|PT\d{23}|('
                                  '?:BE|IS)\d{24}|(?:FR|MR|MC)\d{25}|('
                                  '?:AL|DO|LB|PL)\d{26}|(?:AZ|HU)\d{27}|('
                                  '?:GR|MU)\d{28})$/i', message="Please enter correct IBAN sequence")

PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message=(
                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                 "allowed."))

POSTCODE_REGEX = RegexValidator(regex=r'^[0-9]+$',
                                message=(
                                    "Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))

# Depending on the design choice validators can be created in models.py files
# In that case, this file should hold only regexes and messages
patterns = {"IBAN_REG": {'regex': '/^(?:(?:IT|SM)\d{2}[A-Z]\d{22}|CY\d{'
                                  '2}[A-Z]\d{23}|NL\d{2}[A-Z]{4}\d{'
                                  '10}|LV\d{2}[A-Z]{4}\d{13}|('
                                  '?:BG|BH|GB|IE)\d{2}[A-Z]{4}\d{'
                                  '14}|GI\d{2}[A-Z]{4}\d{15}|RO\d{2}['
                                  'A-Z]{4}\d{16}|KW\d{2}[A-Z]{4}\d{'
                                  '22}|MT\d{2}[A-Z]{4}\d{23}|NO\d{13}|('
                                  '?:DK|FI|GL|FO)\d{16}|MK\d{17}|('
                                  '?:AT|EE|KZ|LU|XK)\d{18}|('
                                  '?:BA|HR|LI|CH|CR)\d{19}|('
                                  '?:GE|DE|LT|ME|RS)\d{20}|IL\d{21}|('
                                  '?:AD|CZ|ES|MD|SA)\d{22}|PT\d{23}|('
                                  '?:BE|IS)\d{24}|(?:FR|MR|MC)\d{25}|('
                                  '?:AL|DO|LB|PL)\d{26}|(?:AZ|HU)\d{27}|('
                                  '?:GR|MU)\d{28})$/i',
                         'message': "Please enter correct IBAN sequence"},
            }
