from django.db import models

from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from customers.models import City, Customer
from baskets.models import Basket


class BillingAddress(BaseAbstractModel):
    """
    Stores billing address, relates to :model:`customers.City`
    """
    full_name = models.CharField(_("Full Name"), max_length=50)
    line_1 = models.CharField(_("Line 1"), max_length=200)
    line_2 = models.CharField(_("Line 2"), max_length=200)
    phone = models.CharField(_("Phone Number"), max_length=50)
    district = models.CharField(_("District"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.city} - {self.district} - {self.phone}"


class InvoiceAddress(BaseAbstractModel):
    """
    Stores invoice address, relates to :model:`customers.City`
    """
    full_name = models.CharField(_("Full Name"), max_length=50)
    line_1 = models.CharField(_("Line 1"), max_length=200)
    line_2 = models.CharField(_("Line 2"), max_length=200)
    phone = models.CharField(_("Phone Number"), max_length=50)
    district = models.CharField(_("District"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.city} - {self.district} - {self.phone}"


class OrderBankAccount(BaseAbstractModel):
    """
    Stores order bank accounts, related to :model:`orders.Order`
    """
    name = models.CharField(_("Name"), max_length=50)
    # IBAN field should be changed in a more secure version before deployment
    iban = models.CharField(_("IBAN"), max_length=50)
    bank_name = models.CharField(_("Bank Name"), max_length=50)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f"{self.name} - {self.order}"


class Order(BaseAbstractModel):
    """
    Stores individual orders, related to :model:`baskets.Basket` and
    `customers.Customer`
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    billing_address = models.CharField(_("Billing Address"), max_length=200)
    shipping_address = models.CharField(_("Shipping Address"), max_length=200)
    # total_price should be calculated 
    total_price = models.DecimalField(verbose_name=_("Total Price"),
                                      max_digits=10,
                                      decimal_places=2)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket}"


class OrderItem(BaseAbstractModel):
    """
    Stores items in the basket, relates to :model:`orders.Order`
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(_("Product"), max_length=50)
    price = models.DecimalField(verbose_name=_("Price"),
                                max_digits=10,
                                decimal_places=2)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Orders Items")

    def __str__(self):
        return f"{self.order} - {self.product} - {self.price}"
