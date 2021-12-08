from django.db import models
from customers.models import Customer
from baskets import enums
from products.models import Product
from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer, null =True,
                                 on_delete=models.CASCADE,blank=True)
    status = models.CharField(choices=enums.Status.choices, max_length=20, verbose_name=_("Status"),)
    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")
    def __str__(self):
        return f"{self.customer} - {self.status}"
class BasketItem(BaseAbstractModel):
    basket      = models.ForeignKey(Basket, verbose_name=_("Basket"),
                                    on_delete=models.CASCADE)
    product     = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField(verbose_name=_("Quantity"))
    price       = models.DecimalField(verbose_name=("Price"),
                                      max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.basket} - {self.price}"
