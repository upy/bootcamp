from django.db import models
from customers.models import Customer, City
from baskets.models import Basket
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from core.models import BaseAbstractModel
from products.models import Product
from django.utils import timezone

class BillingAddress(BaseAbstractModel):

    city = models.ForeignKey(City, on_delete=models.PROTECT)

    full_name = models.CharField(max_length=127,verbose_name=_("Full_name"))
    address1 = models.CharField(max_length=1024, verbose_name=_("Address line 1"))
    address2 = models.CharField(max_length=1024, null = True, verbose_name=_("Address line 2"))
    phone_validator = RegexValidator(regex=r'^[0-9]+$',
                                 message="Phone number must be entered as all numeric"
                                         "in the format 05555555555"
                                         "up to 16 digits")
    phone = models.CharField(validators=[phone_validator], max_length=16, verbose_name=_("Phone"))
    discrict = models.CharField(max_length=127, verbose_name=("Discrict"))

    postcode_validator = RegexValidator(regex=r'^[0-9]+$',
                                 message="Postcode must be entered as all numeric "
                                         "up to 10 digits 0123456789" )
    postcode = models.CharField(validators=[postcode_validator], max_length=10, verbose_name=_("Postcode"))


    class Meta:
        verbose_name = _("billingaddress")
        verbose_name_plural = _("billingaddresses")

    def __str__(self):
        return f"{self.fullname} - {self.city}"

class ShippingAddress(BaseAbstractModel):

    city = models.ForeignKey(City, on_delete=models.PROTECT)

    full_name = models.CharField(max_length=127,verbose_name=_("full_name"))
    address1 = models.CharField(max_length=1024, verbose_name=_("Address line 1"))
    address2 = models.CharField(max_length=1024, null = True, verbose_name=_("Address line 2"))

    phone_validator = RegexValidator(regex=r'^[0-9]+$',
                                 message="Phone number must be entered as all numeric"
                                         "in the format 05555555555"
                                         "up to 16 digits")
    phone = models.CharField(validators=[phone_validator], max_length=16, verbose_name="phone")
    discrict = models.CharField(max_length=127, verbose_name=("Discrict"))
    postcode_validator = RegexValidator(regex=r'^[0-9]+$',
                                 message="Postcode must be entered as all numeric "
                                         "up to 10 digits 0123456789" )
    postcode = models.CharField(validators=[postcode_validator], max_length=10, verbose_name="postcode")


    class Meta:
        verbose_name = _("shippingaddress")
        verbose_name_plural=  _("shippingaddresses")
    def __str__(self):
        return f"{self.fullname} - {self.city}"



class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.PROTECT)

    basket = models.ForeignKey(Basket, verbose_name=_("Basket"), on_delete=models.PROTECT)

    billing_address = models.OneToOneField(BillingAddress, verbose_name=_("Billing Address"), on_delete=models.PROTECT)
    shipping_address = models.OneToOneField(ShippingAddress, verbose_name=_("Shipping Address"), on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket} - {self.total_price}"



class OrderBankAccount(BaseAbstractModel):

    name = models.CharField(max_length=255,null=False)
    iban_validator = RegexValidator(regex=r'^[A-Za-z0-9]+$',
                                 message="iban must be an alphanumeric value "
                                         "34 characters at most" )
    iban = models.CharField(validators=[iban_validator], max_length=34, verbose_name="iban")
    bank_name = models.CharField(max_length=255, verbose_name=_("Bank Name"))
    class Meta:
        verbose_name = _("Order Bank Account")
    def __str__(self):
        return f"{self.name} - {self.bank_name}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
    def __str__(self):
        return f"{self.order} - {self.product}"

