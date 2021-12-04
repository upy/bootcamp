from django.db import models
from django.utils.translation import gettext_lazy as _

from baskets import enums
from core.models import BaseAbstractModel
from customers.models import Customer
from products.models import Product

#basket class keeps  foreign key to customer
class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer,
                                verbose_name=_("Customer"),
                                null=True,
                                on_delete=models.CASCADE)
    status = models.CharField(max_length=100,
                              choices=enums.Status.choices,
                              verbose_name=_("Status"))

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


#basketitem class that keeps  foreign key to customer and basket
class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket,
                               verbose_name=_("Basket"),
                               max_length=100,
                               on_delete=models.CASCADE,
                               null=True)
    product = models.ForeignKey(Product,
                                verbose_name=_("Product"),
                                max_length=100,
                                on_delete=models.CASCADE,
                                null=True)
    quantity = models.PositiveSmallIntegerField(verbose_name=_("Quantity"))
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name=_("Price"))

    class Meta:
        verbose_name = _("Basket Item")
        verbose_name_plural = _("Basket Items")

    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.price}"

# Create your models here.