from django.db import models
from django.utils.translation import gettext_lazy as _

from baskets.models import Basket
from core.models import BaseAbstractModel
from customers.models import City, Customer
from payments.models import Bank
from products.models import Product


class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line1 = models.CharField(max_length=255, verbose_name=_("Line1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Line2"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    post_code = models.IntegerField(verbose_name=_("Post Code"))
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.phone}"


class ShippingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line1 = models.CharField(max_length=255, verbose_name=_("Line1"))
    line2 = models.CharField(max_length=255, verbose_name=_("Line2"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    post_code = models.IntegerField(verbose_name=_("Post Code"))
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Shipping Address")
        verbose_name_plural = _("Shipping Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.phone}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name="Customer", on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket, verbose_name="Basket", on_delete=models.PROTECT)
    billing_address = models.OneToOneField(BillingAddress, verbose_name="Billing Address", on_delete=models.PROTECT)
    shipping_address = models.OneToOneField(ShippingAddress, verbose_name="Shipping Address", on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Order")

    def __str__(self):
        return f"{self.customer} - {self.basket}"


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    iban = models.CharField(max_length=26, verbose_name=_("Iban"))
    bank = models.ForeignKey(Bank, verbose_name="Bank", on_delete=models.PROTECT)
    order = models.ForeignKey(Order, verbose_name="Order", on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Account")

    def __str__(self):
        return f"{self.name} - {self.bank}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name="Order", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Item")

    def __str__(self):
        return f"{self.order} - {self.product}"
