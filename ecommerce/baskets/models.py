from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseAbstractModel

from customers.models import Customer
from products.models import Product
from baskets import enums


class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer,
                                 verbose_name=_("Customer"),
                                 on_delete=models.CASCADE,
                                 null=True)
    status = models.CharField(max_length=50,
                              verbose_name=_("Status"),
                              choices=enums.Status.choices
                              )

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")

    def __str__(self):
        return f"{self.customer} : {self.status}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket,
                               verbose_name=_("Basket"),
                               on_delete=models.CASCADE,
                               null=True)
    product = models.ForeignKey(Product,
                                verbose_name=_("Product"),
                                on_delete=models.CASCADE,
                                null=True)
    quantity = models.PositiveSmallIntegerField(default=0,
                                                verbose_name=_("Quantity"))
    price = models.DecimalField(default=0,
                                max_digits=10,
                                decimal_places=2,
                                verbose_name=_("Price"))

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return f"{self.product} : {self.quantity} : {self.price}"
