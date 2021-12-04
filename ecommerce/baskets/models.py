from django.db import models
from django.utils.translation import gettext_lazy as _

from customers.models import Customer
from products.models import Product
from core.models import BaseAbstractModel
from baskets import enums


class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"),
                                   null=True, on_delete=models.DO_NOTHING)
    status = models.CharField(
        choices=enums.Statuses.choices, verbose_name=_("Status"), max_length=20)

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"),
                               on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, verbose_name=_("Product"),
                                on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"),)
    price = models.DecimalField(verbose_name=_("Price"),
                                max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("basketItem")
        verbose_name_plural = _("basketItems")

    def __str__(self):
        return f"{self.product} - {self.quantity}"