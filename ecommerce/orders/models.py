from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.generic.models import IBANField

from baskets.models import Basket
from core.models import BaseAbstractModel
from customers.models import Address, Customer
from products.models import Product


class BillingAddress(Address):
    pass


class ShippingAddress(Address):
    pass


class Order(BaseAbstractModel):

    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket, verbose_name=_('Basket'), on_delete=models.PROTECT)
    billing_address = models.ForeignKey(BillingAddress, verbose_name=_("Billing Address"), on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(ShippingAddress, verbose_name=_("Shipping Address"), on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f'{self.customer} - {self.created_at}'


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def __str__(self):
        return f'{self.order} - {self.product} - {self.price}'


class OrderBankAccount(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    bank_name = models.CharField(max_length=255, verbose_name=_("Bank Name"))
    iban = IBANField()

    class Meta:
        verbose_name = _("order bank account")
        verbose_name_plural = _("order bank accounts")

    def __str__(self):
        return f'{self.name} - {self.order}'
