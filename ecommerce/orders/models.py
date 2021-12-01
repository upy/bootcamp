from django.db import models

from baskets.models import Basket
from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _

from customers.models import City, Customer
from payments.models import Bank
from products.models import Product


class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(
        "Full name",
        max_length=255,
    )
    line_1 = models.CharField(
        "Address Line 1",
        max_length=255,
    )
    line_2 = models.CharField(
        "Address Line 2",
        max_length=255,
    )
    phone = models.CharField(
        "Phone number",
        max_length=16,
    )
    district = models.CharField(
        "District",
        max_length=255,
    )
    postcode = models.CharField(
        "Post code",
        max_length=10,
    )
    city = models.ForeignKey(City, verbose_name=_("City"),
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("billing address")
        verbose_name_plural = _("billing addresses")

    def __str__(self):
        return f"{self.full_name}"


class InvoiceAddress(BaseAbstractModel):
    full_name = models.CharField(
        "Full name",
        max_length=255,
    )
    line_1 = models.CharField(
        "Address Line 1",
        max_length=255,
    )
    line_2 = models.CharField(
        "Address Line 2",
        max_length=255,
    )
    phone = models.CharField(
        "Phone number",
        max_length=16,
    )
    district = models.CharField(
        "District",
        max_length=255,
    )
    postcode = models.CharField(
        "Post code",
        max_length=10,
    )
    city = models.ForeignKey(City, verbose_name=_("City"),
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("invoice address")
        verbose_name_plural = _("invoice addresses")

    def __str__(self):
        return f"{self.full_name}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"),
                                 on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"),
                               on_delete=models.PROTECT)
    billing_address = models.ForeignKey(BillingAddress, verbose_name=_("Billing Address"),
                                        on_delete=models.PROTECT)
    shipping_address = models.CharField(max_length=255, verbose_name=_("Shipping Address"))
    total_price = models.DecimalField(verbose_name=_("Total Order Price"),
                                      max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.customer} - {self.basket}"


class OrderBankAccount(BaseAbstractModel):
    bank = models.ForeignKey(Bank, verbose_name=_("Bank"),
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_("Order Bank Account Name"))
    iban = models.CharField(max_length=255, verbose_name=_("IBAN Number"))
    order = models.ForeignKey(Order, verbose_name=_("Order"),
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("bank account")
        verbose_name_plural = _("bank accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name=_("Order"),
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"),
                                on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name=_("Order Item Price"),
                                max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def __str__(self):
        return f"{self.order} - {self.product}"
