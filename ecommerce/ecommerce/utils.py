class Regex:
    IBAN = r'\b[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?!(?:[ ]?[0-9]){3})(?:[ ]?[0-9]{1,2})?\b'
    PHONE = r'^\+(\d{2})\s\((\d{3})\)\s(\d{3})\s(\d{2})\s(\d{2})'
    POSTCODE = r'\d{5}'


class ValidatorMessage:
    IBAN = "iban must be entered in the format: '9999999999999999999999'\n or in the format: \'9999 9999 9999 9999 " \
           "9999 99\'. "
    PHONE = "Phone number must be entered in the format: '+99 (999) 999 99 99'."
    POSTCODE = "postcode must be entered in the format: '99999'."
