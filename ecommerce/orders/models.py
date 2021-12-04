from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from basket.models import Basket
from core.models import BaseAbstractModel
from customers.models import Address, Customer
from ecommerce.utils import Regex, ValidatorMessage
from products.models import Product


class BillingAddress(Address):
    class Meta:
        verbose_name = _("billing address")
        verbose_name_plural = _("billing addresses")

    def __str__(self):
        return f"{self.customer.email} - 'billing-address'- {self.city}"


class ShippingAddress(Address):
    class Meta:
        verbose_name = _("shipping address")
        verbose_name_plural = _("shipping addresses")

    def __str__(self):
        return f"{self.customer.email} - 'shipping-address' - {self.city}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name=_("Customer")
    )
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE,
        verbose_name=_("Basket")
    )
    billing_address = models.ForeignKey(
        BillingAddress,
        on_delete=models.CASCADE,
        verbose_name=_("Billing Address")
    )
    shipping_address = models.ForeignKey(
        ShippingAddress,
        on_delete=models.CASCADE,
        verbose_name=_("Shipping Address")
    )
    total_price = models.PositiveIntegerField(verbose_name=_("Total Price"))

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.basket} - total price: {self.total_price}"


class OrderBankAccount(BaseAbstractModel):
    iban_regex = RegexValidator(regex=Regex.IBAN,
                                message=ValidatorMessage.IBAN)
    iban = models.CharField(validators=[iban_regex], max_length=27)
    bank_name = models.CharField(verbose_name=_("Bank Name"), max_length=100)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_("Order")
    )

    class Meta:
        verbose_name = _("order bank account")
        verbose_name_plural = _("order bank accounts")
        db_table = "bank_account"

    def __str__(self):
        return f"{self.iban} - {self.bank_name}"


class OrderItem(BaseAbstractModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("Product")
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_("Order")
    )

    price = models.PositiveIntegerField(verbose_name=_("Price"))

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        unique_together = ['product', 'order']

    def __str__(self):
        return f"{self.product} - {self.order}"
