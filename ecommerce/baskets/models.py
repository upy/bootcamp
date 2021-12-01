from django.db import models

from baskets import enums
from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _

from customers.models import Customer
from products.models import Product


class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"),
                                 on_delete=models.CASCADE, null=True)
    status = models.CharField(
        choices=enums.Status.choices, verbose_name=_("Status"), max_length=20)

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"),
                               on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"),
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    price = models.PositiveIntegerField(verbose_name=_("Price"))

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")

    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.price}"
