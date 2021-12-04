from django.core.validators import RegexValidator
from django.db import models

from django.utils.translation import gettext_lazy as _

from baskets.models import Basket
from core.models import BaseAbstractModel
from customers.models import City, Customer

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                     "allowed.")

class BillingAddress(BaseAbstractModel):

    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=500, verbose_name=_("Line 1"))
    line_2 = models.CharField(max_length=500, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=30, validators=[phone_regex], verbose_name=_("Phone Number"))
    district = models.CharField(max_length=100, verbose_name=_("District"))
    postcode = models.CharField(max_length=100, verbose_name=_("Postcode"))
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1} - {self.line_2} - {self.city} - {self.district} - {self.phone}"


class ShippingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=500, verbose_name=_("Line 1"))
    line_2 = models.CharField(max_length=500, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=30, validators=[phone_regex], verbose_name=_("Phone Number"))
    district = models.CharField(max_length=100, verbose_name=_("District"))
    postcode = models.CharField(max_length=100, verbose_name=_("Postcode"))
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Shipping Address")
        verbose_name_plural = _("Shipping Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1} - {self.line_2} - {self.city} - {self.district} - {self.phone}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, )
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, )
    billing_address = models.CharField(max_length=255, verbose_name=_("Billing Address"))
    shipping_address = models.CharField(max_length=255, verbose_name=_("Shipping Address"))
    total_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Total Price"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket} - {self.total_price}"

class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=50, verbose_name=_("Product"))
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Price"))

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.order} - {self.product} - {self.price}"


class OrderBankAccount(BaseAbstractModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    iban = models.CharField(max_length=50, verbose_name="IBAN", null=False)
    bank_name = models.CharField(max_length=50, verbose_name=_("Bank Name"))

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f"{self.order} - {self.name} - {self.iban} - {self.bank_name}"
