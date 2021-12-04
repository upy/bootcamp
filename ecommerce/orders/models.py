from django.db import models
from django.utils.translation import gettext_lazy as _
from baskets.models import Basket
from core.models import BaseAbstractModel, BaseAbstractAddressModel
from customers.models import Customer
from payments.models import BankAccount
from products.models import Product


class BillingAddress(BaseAbstractAddressModel):  # Inherited from core app model BaseAbstractAddressModel
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("billing address")
        verbose_name_plural = _("billing addresses")

    def __str__(self):
        return super().__str__()


class ShippingAddress(BaseAbstractAddressModel):  # Inherited from core app model BaseAbstractAddressModel
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("shipping address")
        verbose_name_plural = _("shipping addresses")

    def __str__(self):
        return super().__str__()


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT)
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"),
                                 max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.customer.first_name} - {self.customer.last_name} - {self.billing_address} - {self.shipping_address} - {self.total_price}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_("Price"),
                                 max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def __str__(self):
        return f"{self.product} - {self.price}"

class OrderBankAccount(BankAccount): # Inherited from payments app model BankAccount
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("order bank account")
        verbose_name_plural = _("order bank accounts")

    def __str__(self):
        return super().__str__()