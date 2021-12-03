from django.db import models
from customers.models import Customer
from products.models import Product
from baskets import enums
from django.utils.translation import gettext_lazy as _


class Basket(models.Model):
    """
    Basket model for customer's products\n
    Required Fields: status\n
    Optional Fields: customer\n
    One to many relation with Customer model from customers app
    """
    # null might be wrong in customer field
    customer = models.ForeignKey(Customer, null=True, on_delete=models.DO_NOTHING)
    status = models.CharField(
        choices=enums.Status.choices, verbose_name=_("Status"), max_length=20)

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer}-{self.status}"


class BasketItem(models.Model):
    """
    BasketItem model for customer's basket\n
    Required Fields: basket, product, quantity, price\n
    Optional Fields: none\n
    One to many relation with Basket model and Product model from products app
    """
    # null might be wrong in customer field
    basket = models.ForeignKey(Basket, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(verbose_name=_("quantity"))
    price = models.DecimalField(verbose_name=_("price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")

    def __str__(self):
        return f"{self.basket}- {self.product}"