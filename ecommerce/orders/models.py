from django.db import models
from core.models import BaseAbstractModel
# from django import forms  # Import forms library to use forms.RegexField for Address.phone
from customers.models import City
from django.utils.translation import gettext_lazy as _
from customers.models import Customer
from baskets.models import Basket
from products.models import Product
from payments.models import BankAccount, Bank
from django.core.validators import RegexValidator  # Import forms library to use forms.RegexField for Address.phone/postcode


class BillingAddress(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    full_name = models.CharField(verbose_name=_("full name"), max_length=200)
    line1 = models.CharField(verbose_name=_("line1"), max_length=250)
    line2 = models.CharField(verbose_name=_("line2"), max_length=250)
    phone_regex = RegexValidator(regex=r'^[0-9]+$',
                                 message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits "
                                         "allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, verbose_name='phone')
    district = models.CharField(verbose_name=_("district"), max_length=100)
    postcode_regex = RegexValidator(regex=r'^[0-9]+$', message=("Postal Code must be entered in the format: "
                                                                "'1234567'. Up to 7 digits allowed."))
    postcode = models.CharField(validators=[postcode_regex], max_length=7, verbose_name='Postal code')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.district}"


class ShippingAddress(BaseAbstractModel):  # InvoiceAddress' name is changed to ShippingAddress
    """
    returns: __str__(self)
    params: BaseAbstractModel Class, forms.ModelForm Class
    """
    full_name = models.CharField(verbose_name=_("full name"), max_length=200)
    line1 = models.CharField(verbose_name=_("line1"), max_length=250)
    line2 = models.CharField(verbose_name=_("line2"), max_length=250)
    phone_regex = RegexValidator(regex=r'^[0-9]+$',
                                 message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits "
                                         "allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, verbose_name='phone')
    district = models.CharField(verbose_name=_("district"), max_length=100)
    postcode_regex = RegexValidator(regex=r'^[0-9]+$', message=("Postal Code must be entered in the format: "
                                                                "'1234567'. Up to 7 digits allowed."))
    postcode = models.CharField(validators=[postcode_regex], max_length=7, verbose_name='Postal code')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.district}"


class Order(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    total_price = models.DecimalField(verbose_name=_("total price"), max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer} - {self.basket}"


class OrderBankAccount(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    name = models.CharField(verbose_name=_("name"), max_length=50)
    iban = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrderItem(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_("price"), max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order)
