from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from baskets import enums

from customers.models import Customer
from products.models import Product


# Basket Model
class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE, null=True)

    status = models.CharField(choices=enums.Status.choices, verbose_name=_("Status"), max_length=20)

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


# Basket item model
class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"), on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(verbose_name=_("Quantity"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.price}"
