from django.core.validators import RegexValidator


def validatePhoneNumber():
    return RegexValidator(regex=r'^[0-9]+$', message=(
        "Phone number should only contain 0-9 and +.Maximum of 15 digits."))


def validatePostCode():
    return RegexValidator(regex=r'^[0-9]$', message=(
        "Postal Code should only contain 0-9 .Maximum of 7 digits."))

def validateIBANNumber():
    return RegexValidator(regex=r'^[A-Z]{2}[a-zA-Z0-9]{10,34}$', message=(
        "Iban should only 2 chars for country and remaining 32 characters should contain 0-9, A-Z .Maximum of 34 characters."))