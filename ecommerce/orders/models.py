from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from orders import enums
from django.core.validators import RegexValidator

iban_validator = RegexValidator(regex=r'^[A-Z]{2}[0-9]{2}[A-Z0-9]{4}[0-9]{7}([A-Z0-9]?){0,16}$', message=_('Enter a valid IBAN number.'))
phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
postcode_validator = RegexValidator(regex=r'^[0-9]+$', message=( "Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))


# Model for Billing address
class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=255, verbose_name=_("Address Line 1"))
    line_2 = models.CharField(max_length=255, verbose_name=_("Address Line 2"), blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name=_("Phone Number"), validators=[phone_validator])
    district = models.CharField(max_length=255, verbose_name=_("District"))
    postcode = models.CharField(max_length=20, verbose_name=_("Post Code"), blank=True, validators=[postcode_validator])
    city = models.ForeignKey("customers.City", verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1} - {self.line_2} - {self.district} - {self.city}"


# Model for Shipping Address
class ShippingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    line_1 = models.CharField(max_length=255, verbose_name=_("Address Line 1"))
    line_2 = models.CharField(max_length=255, verbose_name=_("Address Line 2"), blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name=_("Phone Number"), validators=[phone_validator])
    district = models.CharField(max_length=255, verbose_name=_("District"))
    postcode = models.CharField(max_length=20, verbose_name=_("Post Code"), blank=True, validators=[postcode_validator])
    city = models.ForeignKey("customers.City", verbose_name=_("City"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Shipping Address")
        verbose_name_plural = _("Shipping Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line_1} - {self.line_2} - {self.district} - {self.city} - {self.phone}"


# Model for order bank account
class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    iban = models.CharField(max_length=50, verbose_name=_("IBAN"), validators=[iban_validator])
    bank_name = models.CharField(max_length=100, verbose_name=_("Bank Name"))
    order = models.ForeignKey("orders.Order", verbose_name=_("Order"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f"{self.name} - {self.order}"


# Model for order
class Order(BaseAbstractModel):

    customer = models.ForeignKey("customers.Customer", verbose_name=_("Customer"), on_delete=models.PROTECT)
    basket = models.ForeignKey("baskets.Basket", verbose_name=_("Basket"), on_delete=models.PROTECT)
    status = models.CharField(choices=enums.OrderStatus.choices, max_length=20, verbose_name=_("Order Status"))
    billing_address = models.ForeignKey(BillingAddress, verbose_name=_("Billing Address"), on_delete=models.PROTECT, max_length=200)
    shipping_address = models.ForeignKey(ShippingAddress, verbose_name=_("Shipping Address"), on_delete=models.PROTECT, max_length=200)
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket}"


# Model for Order Item
class OrderItem(BaseAbstractModel):

    order = models.ForeignKey("Order", verbose_name=_("Order"), on_delete=models.PROTECT)
    product = models.CharField(max_length=255, verbose_name=_("Product"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.order} - {self.product} - {self.price}"
