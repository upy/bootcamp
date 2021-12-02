from django.db import models
from django.utils.translation import gettext_lazy as _
from customers.models import Customer
from products.models import Product
from core.models import BaseAbstractModel
from baskets import enums

class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("customer"),
                                   on_delete=models.PROTECT, null=True)
    status = models.CharField(choices=enums.Status.choices, verbose_name=_("customer"), max_length=30 )
    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("basket")
    def __str__(self):
        return f"{self.customer} - {self.Status}"

class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket, verbose_name=_("basket"),
                                   on_delete=models.PROTECT)
    product= models.ForeignKey(Product, verbose_name=_("basket"),
                                   on_delete=models.PROTECT)
    quantity = models.DecimalField(verbose_name=_("Quantity"),
                                 max_digits=4, decimal_places=1)
    price = models.DecimalField(verbose_name=_("Price"),
                                   max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("basketItem")
        verbose_name_plural = _("basketItems")
    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.price}"

