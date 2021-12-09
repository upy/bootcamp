from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils import phonenumber_validator, iban_validator
from core.models import BaseAbstractModel
from orders import enums
from orders.managers import BillingAddressQuerySet, ShippingAddressQuerySet, \
    OrderQuerySet, OrderBankAccountQuerySet, OrderItemQuerySet


class BillingAddress(BaseAbstractModel):
    """
    Billing Address Model
    """
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=255, verbose_name=_("Address Line 1"))
    line_2 = models.CharField(max_length=255, verbose_name=_("Address Line 2"), blank=True, null=True)
    phone = models.CharField(
        max_length=20, verbose_name=_("Phone Number"), validators=[phonenumber_validator])
    district = models.CharField(max_length=255, verbose_name=_("District"))
    zipcode = models.CharField(max_length=20, verbose_name=_("Zip Code"))
    city = models.ForeignKey("customers.City", verbose_name=_("City"), on_delete=models.PROTECT)
    objects = BillingAddressQuerySet.as_manager()

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1} - {self.line_2} - {self.district} - {self.city}"


class ShippingAddress(BaseAbstractModel):
    """
    Shipping Address Model
    """
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=255, verbose_name=_("Address Line 1"))
    line_2 = models.CharField(max_length=255, verbose_name=_("Address Line 2"), blank=True, null=True)
    phone = models.CharField(
        max_length=20, verbose_name=_("Phone Number"), validators=[phonenumber_validator])
    district = models.CharField(max_length=255, verbose_name=_("District"))
    zipcode = models.CharField(max_length=20, verbose_name=_("Zip Code"), blank=True)
    city = models.ForeignKey("customers.City", verbose_name=_("City"), on_delete=models.PROTECT)
    objects = ShippingAddressQuerySet.as_manager()

    class Meta:
        verbose_name = _("Shipping Address")
        verbose_name_plural = _("Shipping Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1} - {self.line_2} - {self.district} - {self.city}"


class OrderBankAccount(BaseAbstractModel):
    """
    Order Bank Account Model
    """
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    iban = models.CharField(max_length=100, verbose_name=_("IBAN"), validators=[iban_validator])
    bank_name = models.CharField(max_length=100, verbose_name=_("Bank Name"))
    order = models.ForeignKey("orders.Order", verbose_name=_("Order"), on_delete=models.PROTECT)
    objects = OrderBankAccountQuerySet.as_manager()

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f"{self.name} - {self.order}"


class Order(BaseAbstractModel):
    """
    Order Model
    """
    customer = models.ForeignKey("customers.Customer", verbose_name=_("Customer"), on_delete=models.PROTECT)
    basket = models.ForeignKey("baskets.Basket", verbose_name=_("Basket"), on_delete=models.PROTECT)
    status = models.CharField(choices=enums.OrderStatus.choices,
                              default=enums.OrderStatus.PENDING, max_length=20, verbose_name=_("Status"))
    billing_address = models.ForeignKey(
        BillingAddress, verbose_name=_("Billing Address"), on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(
        ShippingAddress, verbose_name=_("Shipping Address"), on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)
    objects = OrderQuerySet.as_manager()

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket}"


class OrderItem(BaseAbstractModel):
    """
    Order Item Model
    """
    order = models.ForeignKey("Order", verbose_name=_("Order"), on_delete=models.PROTECT)
    product = models.CharField(max_length=255, verbose_name=_("Product"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)
    objects = OrderItemQuerySet.as_manager()

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.order} - {self.product} - {self.price}"
