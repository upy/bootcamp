from django.db import models
from basket.models import Basket
from core.models import BaseAbstractModel
from customers.models import City, Customer
from django.utils.translation import gettext_lazy as _

class BillingAddress(BaseAbstractModel):
    fullName = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line1 = models.CharField(max_length=255, verbose_name=_("Address Line 1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Address Line 2"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    postcode = models.PositiveIntegerField(verbose_name=_("Postcode"))
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name=_("City"))

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.fullName} - {self.line1} "


class InvoiceAddress(BaseAbstractModel):
    fullName = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line1 = models.CharField(max_length=255, verbose_name=_("Address Line 1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Address Line 2"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    postcode = models.PositiveIntegerField(verbose_name=_("Postcode"))
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name=_("City"))

    class Meta:
        verbose_name = _("Invoice Address")
        verbose_name_plural = _("Invoice Addresses")

    def __str__(self):
        return f"{self.fullName} - {self.line1} "


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT)
    billing_address = models.CharField(max_length=255, verbose_name=_("Billing Address"))
    shipping_address = models.CharField(max_length=255, verbose_name=_("Shipping Address"))
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket} "


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    iban = models.PositiveIntegerField(verbose_name=_("Iban"))
    bank_name = models.CharField(max_length=255, verbose_name=_("Bank Name"))
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f"{self.name} - {self.order} "


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.CharField(max_length=255, verbose_name=_("Product"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.order} - {self.product} "
