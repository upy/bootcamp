from django.db import models
from core.models import AddressAbstractModel, BankAccountAbstractModel
from django.utils.translation import gettext_lazy as _
from customers.models import Customer
from baskets.models import Basket
from products.models import Product
from customers.models import City
from payments.models import Bank


class BillingAddress(AddressAbstractModel):
    """
    BillingAddress Model for bill's address\n
    Required Fields: line1, district, post_code, city\n
    Optional Fields: full_name, line2, phone\n
    One to many relation with City model.
    """
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("billing address")
        verbose_name_plural = _("billing addresses")

    def __str__(self):
        return self.full_name


class ShippingAddress(AddressAbstractModel):
    """
    ShippingAddress Model\n
    Required Fields: line1, district, post_code, city\n
    Optional Fields: full_name, line2, phone\n
    One to many relation with City model.
    """
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("invoice address")
        verbose_name_plural = _("invoice addresses")

    def __str__(self):
        return self.full_name


class Order(models.Model):
    """
    Order Model\n
    Required Fields: customer, basket, billing_address, shipping_address, total_price\n
    Optional Fields: none\n
    One to many relation with OrderBankAccount, OrderItem.
    """
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    basket = models.ForeignKey(Basket, on_delete=models.DO_NOTHING)
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.DO_NOTHING)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.DO_NOTHING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return self.customer


class OrderBankAccount(BankAccountAbstractModel):
    """
    OrderBankAccount for orders\n
    Required Fields: bank, name, iban, order\n
    Optional Fields: none\n
    """
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("order bank account")
        verbose_name_plural = _("order bank accounts")

    def __str__(self):
        return f"{self.bank}-{self.name}"


class OrderItem(models.Model):
    """
    Order Item\n
    Required Fields: order, product, price\n
    Optional Fields: none\n
    """
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def __str__(self):
        return f"{self.order}-{self.product}"
