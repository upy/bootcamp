from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from customers.models import City, Customer
from baskets.models import Basket


class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=50, verbose_name=_("Full Name"))
    line1 = models.CharField(max_length=255, verbose_name=_("Line 1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    district = models.CharField(max_length=25, verbose_name=_("District"))
    postcode = models.CharField(max_length=10, verbose_name=_("Postcode"))
    city = models.ForeignKey(City, verbose_name=_("City"),
                                   on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("billingAddress")
        verbose_name_plural = _("billingAddresses")

    def __str__(self):
        return f"{self.full_name}"


class InvoiceAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=50, verbose_name=_("Full Name"))
    line1 = models.CharField(max_length=255, verbose_name=_("Line 1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    district = models.CharField(max_length=25, verbose_name=_("District"))
    postcode = models.CharField(max_length=10, verbose_name=_("Postcode"))
    city = models.ForeignKey(City, verbose_name=_("City"),
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("invoiceAddress")
        verbose_name_plural = _("invoiceAddresses")

    def __str__(self):
        return f"{self.full_name}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"),
                                   on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"),
                                 on_delete=models.PROTECT)
    billing_address = models.CharField(max_length=255, verbose_name=_("Billing Address"))
    shipping_address = models.CharField(max_length=255, verbose_name=_("Shipping Address"))
    total_price = models.DecimalField(verbose_name=_("Total Price"),
                                max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.customer} - {self.total_price}"


class OrderBankAccount(BaseAbstractModel):
    bank_name = models.CharField(max_length=50, verbose_name=_("Bank Name"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    iban = models.CharField(max_length=50, verbose_name=_("Iban"))
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("orderBankAccount")
        verbose_name_plural = _("orderBankAccounts")

    def __str__(self):
        return f"{self.name} - {self.order} - {self.bank_name}"


class OrderItem(BaseAbstractModel):
    product = models.CharField(max_length=255, verbose_name=_("Product"))
    price = models.DecimalField(verbose_name=_("Price"),
                                max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, verbose_name=_("Order"),
                              on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("orderItem")
        verbose_name_plural = _("orderItems")

    def __str__(self):
        return f"{self.product} - {self.order} - {self.price}"

