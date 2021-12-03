from django.db import models
from django.utils.translation import gettext_lazy as _

from baskets import enums
from core.models import BaseAbstractModel

from customers.models import Customer
from products.models import Product


class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer,
                                 verbose_name=_("Customer"),
                                 on_delete=models.CASCADE,
                                 null=True
                                 )

    status = models.CharField(choices=enums.Status.choices,
                              verbose_name=_("Status"),
                              max_length=15
                              )

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket,
                               verbose_name=_("Basket"),
                               on_delete=models.CASCADE,
                               null=True
                               )

    product = models.ForeignKey(Product,
                                verbose_name=_("Product"),
                                on_delete=models.CASCADE,
                                )
    # There might be the basket which also used for wishlist.
    # Therefore PositiveSmallIntegerField could be insufficient with its 32767 item size
    # So, PositiveIntegerField is used. quantity and price also can't be null.
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), null=False)

    # price could be maximum 999.999.999,99 unit of money
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=_("Price"))

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")

    # it does make sense that basket items with product, quantity and respective price information.
    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.price}"
