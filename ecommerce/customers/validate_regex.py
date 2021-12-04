from django.core.validators import RegexValidator


def validatePhoneNumber():
    return RegexValidator(regex=r'^[0-9]+$', message=(
        "Phone number should only contain 0-9 and +.Maximum of 15 digits."))


def validatePostCode():
    return RegexValidator(regex=r'^[0-9]$', message=(
        "Postal Code should only contain 0-9 .Maximum of 7 digits."))