from core.models import BaseAbstractModel
from django.db import models
from django.utils.translation import gettext_lazy as _

from baskets.enums import BasketStatus

# Create your models here.

class Basket(BaseAbstractModel):
    customer = models.ForeignKey(
        "customers.Customer",
        verbose_name=_("Customer"),
        on_delete=models.CASCADE,
        null=True
    )
    status = models.CharField(
        choices=BasketStatus.choices,
        verbose_name=_("Status"),
        max_length=20
    )

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")

    def __str__(self):
        return f"{self.customer} - {self.get_status_display()}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(
        "baskets.Basket",
        verbose_name=_("Basket"),
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
        default=1
    )
    price = models.PositiveIntegerField(
        verbose_name=_("Price")
    )

    class Meta:
        verbose_name = _("Basket Item")
        verbose_name_plural = _("Basket Items")

    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.price}"
