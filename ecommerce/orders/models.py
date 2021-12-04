from core.models import (AddressAbstractModel, BankAccountAbstractModel,
                         BaseAbstractModel)
from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.enums import OrderStatusEnum


class BillingAddress(AddressAbstractModel):

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name}"


class ShippingAddress(AddressAbstractModel):

    class Meta:
        verbose_name = _("Shipping Address")
        verbose_name_plural = _("Shipping Addresses")

    def __str__(self):
        return f"{self.full_name}"


class Order(BaseAbstractModel):
    status = models.CharField(
        choices=OrderStatusEnum.choices,
        default=OrderStatusEnum.PAYMENT_WAITING,
        max_length=2
    )
    customer = models.ForeignKey(
        "customers.Customer",
        verbose_name=_("Customer"),
        on_delete=models.CASCADE
    )
    basket = models.ForeignKey(
        "baskets.Basket",
        verbose_name=_("Basket"),
        on_delete=models.PROTECT
    )
    billing_address = models.OneToOneField(
        "orders.BillingAddress",
        verbose_name=_("Billing Address"),
        related_name="billing_address_orders",
        on_delete=models.PROTECT
    )
    shipping_address = models.OneToOneField(
        "orders.BillingAddress",
        verbose_name=_("Shipping Address"),
        related_name="shipping_address_orders",
        on_delete=models.PROTECT
    )
    total_price = models.DecimalField(
        verbose_name=_("Total Order Price"),
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer.name} - {self.basket}"


class OrderBankAccount(BankAccountAbstractModel):
    bank = models.ForeignKey(
        "payments.Bank",
        verbose_name=_("Bank Name"),
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        "orders.Order",
        verbose_name=_("Order"),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f"{self.bank} - {self.name} - {self.iban}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(
        "orders.Order",
        verbose_name=_("Order"),
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Product"),
        on_delete=models.PROTECT
    )
    price = models.DecimalField(
        verbose_name=_("Order Item Price"),
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.order} - {self.product}"
