from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from customers.models import Customer
from baskets import enums
from products.models import Product


class Basket(BaseAbstractModel):
    # Do not allow the deletion of a user if they have a basket.
    customer = models.ForeignKey(Customer, null=True, verbose_name=_("Customer"),
                                 on_delete=models.PROTECT)
    status = models.CharField(
        choices=enums.Statuses.choices, verbose_name=_("Status"), max_length=20
    )

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")


class BasketItem(BaseAbstractModel):
    # user models.SET_NULL to keep the quantity and price values in DB
    # even if referenced basket and products are deleted. This will help for future
    # customer data analysis.
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"), null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name=_("Product"), null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")
