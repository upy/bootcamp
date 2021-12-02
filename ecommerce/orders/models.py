from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from customers.models import City
from customers.models import Customer
from baskets.models import Basket


class BillingAddress(BaseAbstractModel):
    fullname = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line1= models.CharField(max_length=255, verbose_name=_("Lime 1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone Number"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    postcode = models.PositiveIntegerField(verbose_name=_("PostCode"))
    city = models.ForeignKey(City, verbose_name=_("City"),
                             on_delete=models.PROTECT)
    class Meta:
        verbose_name = _("billingadress")
        verbose_name_plural = _("billingadresses")
    def __str__(self):
        return self.fullname

class InvoiceAddress(BaseAbstractModel):
    fullname = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line1= models.CharField(max_length=255, verbose_name=_("Lime 1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone Number"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    postcode = models.PositiveIntegerField(verbose_name=_("PostCode"))
    city = models.ForeignKey(City, verbose_name=_("City"),
                             on_delete=models.PROTECT)
    class Meta:
        verbose_name = _("invoiceadress")
        verbose_name_plural = _("invoiceadresses")
    def __str__(self):
        return self.fullname
class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"),
                             on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"),
                                 on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=255, verbose_name=_("Billing Address"))
    shipping_address = models.CharField(max_length=255, verbose_name=_("Shipping Address"))
    total_price= models.PositiveIntegerField()


    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
    def __str__(self):
        return f"{self.customer - self.basket - self.total_price}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name=_("Order"),
                                 on_delete=models.CASCADE)
    product = models.CharField(max_length=255, verbose_name=_("Product"))
    total_price= models.PositiveIntegerField()

    class Meta:
        verbose_name = _("orderitemmodel")
        verbose_name_plural = _("orderitemmodels")

    def __str__(self):
        return f"{self.order - self.total_price}"


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    iban = models.IntegerField()
    bank_name = models.CharField(max_length=255, verbose_name=_("bankname"))
    order = models.ForeignKey(Order, verbose_name=_("City"),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("orderbankaccount")
        verbose_name_plural = _("orderbankaccounts")
    def __str__(self):
        return f"{self.name - self.bank_name - self.order}"