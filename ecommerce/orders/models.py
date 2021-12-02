from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from baskets.models import Basket
from core.models import BaseAbstractModel, AddressAbstractModel
from customers.models import City, Customer
from products.models import Product, Price


class BillingAddress(AddressAbstractModel):
    city = models.ForeignKey(City, verbose_name=_("City"), null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("billing address")
        verbose_name_plural = _("billing addresses")


class ShippingAddress(AddressAbstractModel):
    city = models.ForeignKey(City, verbose_name=_("City"), null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("invoice address")
        verbose_name_plural = _("invoice addresses")


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    # create a regex validator to ensure that the iban is in a valid format
    # 2 letter country code, 2 check digits, up to 30 alphanumeric characters
    iban_regex_validator = RegexValidator(
        regex=r"/^(?:(?:IT|SM)\d{2}[A-Z]\d{22}|CY\d{2}[A-Z]\d{23}|NL\d{2}[A-Z]{4}\d{10}|LV\d{2}[A-Z]{4}\d{13}|(?:BG|BH|GB|IE)\d{2}[A-Z]{4}\d{14}|GI\d{2}[A-Z]{4}\d{15}|RO\d{2}[A-Z]{4}\d{16}|KW\d{2}[A-Z]{4}\d{22}|MT\d{2}[A-Z]{4}\d{23}|NO\d{13}|(?:DK|FI|GL|FO)\d{16}|MK\d{17}|(?:AT|EE|KZ|LU|XK)\d{18}|(?:BA|HR|LI|CH|CR)\d{19}|(?:GE|DE|LT|ME|RS)\d{20}|IL\d{21}|(?:AD|CZ|ES|MD|SA)\d{22}|PT\d{23}|(?:BE|IS)\d{24}|(?:FR|MR|MC)\d{25}|(?:AL|DO|LB|PL)\d{26}|(?:AZ|HU)\d{27}|(?:GR|MU)\d{28})$/i",
        message=_("Enter your IBAN (without spaces) in the appropriate format.")
    )
    iban = models.CharField(validators=[iban_regex_validator], max_length=34, verbose_name=_("IBAN"))
    bank_name = models.CharField(max_length=255, verbose_name=_("Bank Name"))

    class Meta:
        verbose_name = _("order bank account")
        verbose_name_plural = _("order bank accounts")

    def __str__(self):
        return self.iban


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name=_("Customer"))
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT, verbose_name=_("Basket"))
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.PROTECT, verbose_name=_("Billing Address"))
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.PROTECT, verbose_name=_("Shipping Address"))

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("Order"))
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_("Product"))
    price = models.ForeignKey(Price, on_delete=models.PROTECT, verbose_name=_("Price"))

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
