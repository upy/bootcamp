from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from customers.models import Customer
from baskets import enums
from baskets.managers import BasketQuerySet, BasketItemQuerySet
from products.models import Product


class Basket(BaseAbstractModel):
    """
    Basket model
    """
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"),
                                 on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(choices=enums.BasketStatus.choices, max_length=10,
                              verbose_name=_("Basket Status"), default=enums.BasketStatus.OPEN)
    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


class BasketItem(BaseAbstractModel):
    """
    Basket item model
    """
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"), on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    objects = BasketItemQuerySet.as_manager()

    class Meta:
        verbose_name = _("Basket item")
        verbose_name_plural = _("Basket items")

    def __str__(self):
        return f"{self.basket} - {self.product} - {self.quantity} - {self.price}"