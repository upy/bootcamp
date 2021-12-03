from django.db import models
from core.models import BaseAbstractModel
from customers.models import Customer
from django.utils.translation import gettext_lazy as _
from . enums import Status
from products.models import Product


class Basket(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    customer = models.ForeignKey(Customer, null=True, verbose_name=_("Customer"), on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices, verbose_name=_("Status"), max_length=20)

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


class BasketItem(BaseAbstractModel):
    """
    returns: __str__(self)
    params: BaseAbstractModel Class
    """
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")

    def __str__(self):
        return f"{self.basket} - {self.product}"

