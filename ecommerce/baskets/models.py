from django.db import models
from core.models import BaseAbstractModel
from customers.models import Customer
from django.utils.translation import gettext_lazy as _

from products.models import Product

class Status(models.TextChoices):
    OPEN = "open", _("Open")
    SUBMITTED = "submitted", _("Submitted")
    MERGED = "merged", _("Merged")


class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=Status.choices, verbose_name=_("Status"), max_length=20)

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    price = models.DecimalField(verbose_name=_("Amount"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("basketItem")
        verbose_name_plural = _("basketItems")

    def __str__(self):
        return f"{self.basket} - {self.product}"