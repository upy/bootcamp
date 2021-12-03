from django.db import models
from django.utils.translation import gettext_lazy as _
from baskets.models import Basket
from core.models import BaseAbstractModel
from customers.models import City, Customer
from products.models import Product, Price
from django.core.validators import RegexValidator

NUM_REGEX = RegexValidator('^[0-9]*$')


class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=255, verbose_name=_("Line 1"))
    line_2 = models.CharField(max_length=255, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=15, verbose_name=_("Phone"), validators=[NUM_REGEX])
    district = models.CharField(max_length=20, verbose_name=_("District"))
    postcode = models.CharField(max_length=10, verbose_name=_("Postcode"), validators=[NUM_REGEX])
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("billing address")
        verbose_name_plural = _("billing addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1}, {self.line_2} - {self.district}/{self.city} - {self.postcode} - " \
               f"{self.phone}"


class InvoiceAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=255, verbose_name=_("Line 1"))
    line_2 = models.CharField(max_length=255, verbose_name=_("Line 2"))
    phone = models.CharField(max_length=15, verbose_name=_("Phone"), validators=[NUM_REGEX])
    district = models.CharField(max_length=20, verbose_name=_("District"))
    postcode = models.CharField(max_length=10, verbose_name=_("Postcode"), validators=[NUM_REGEX])
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("invoice address")
        verbose_name_plural = _("invoice addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1}, {self.line_2} - {self.district}/{self.city} - {self.postcode} - " \
               f"{self.phone}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"), on_delete=models.PROTECT)
    billing_address = models.ForeignKey(BillingAddress, verbose_name=_("Billing Address"), on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(InvoiceAddress, verbose_name=_("Shipping Address"), on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.customer} - {self.basket} -  {self.shipping_address} - {self.total_price}"


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    iban = models.CharField(max_length=16, validators=[NUM_REGEX], verbose_name="IBAN")
    bank_name = models.CharField(max_length=30, verbose_name=_("Bank Name"))
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("order bank account")
        verbose_name_plural = _("order bank accounts")

    def __str__(self):
        return f"{self.name} - {self.iban} - {self.bank_name} - {self.order}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.PROTECT)
    price = models.ForeignKey(Price, verbose_name=_("Price"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def __str__(self):
        return f"{self.order} - {self.product} - {self.price}"
