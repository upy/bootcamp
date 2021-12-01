from django.db import models
from django.utils.translation import gettext_lazy as _

from basket import enums
from core.models import BaseAbstractModel
from customers.models import Customer
from products.models import Product


class Basket(BaseAbstractModel):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        # related_name=<>
        # related_query_name=<>
        null=True,
        verbose_name="customer"
    )
    status = models.CharField(choices=enums.StatusTypes.choices,
                              verbose_name=_("Status Type"), max_length=20, default=enums.STATUS_TYPE_OPEN)

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer.name} - {self.status}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE,
        # related_name=<>
        # related_query_name=<>
        verbose_name="basket"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        # related_name=<>
        # related_query_name=<>
        verbose_name="product"
    )

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")
        db_table = "basket_basket_item"

    def __str__(self):
        return f"{self.basket} - {self.product}"
