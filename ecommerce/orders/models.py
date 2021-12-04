from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseAbstractAddressModel, BaseAbstractModel
from core.regex_validators import IBAN_REGEX
from customers.models import Customer
from baskets.models import Basket
from products.models import Product


class BillingAddress(BaseAbstractAddressModel):
    class Meta:
        verbose_name = _('billing address')
        verbose_name_plural = _("billing addresses")

    def __str__(self):
        return f"{self.full_name} - {self.phone_number} - {self.city}/{self.district}/{self.postal_code}"


class ShippingAddress(BaseAbstractAddressModel):
    class Meta:
        verbose_name = _('invoice address')
        verbose_name_plural = _("invoice addresses")

    def __str__(self):
        return f"{self.full_name} - {self.phone_number} - {self.city}/{self.district}/{self.postal_code}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_('Customer'), on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, verbose_name=_('Basket'), on_delete=models.CASCADE)
    billing_address = models.OneToOneField(BillingAddress, verbose_name=_('Billing Address'), on_delete=models.PROTECT)
    shipping_address = models.OneToOneField(ShippingAddress, verbose_name=_('Shipping Address'),
                                            on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.customer} - {self.basket}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name=_('Order'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE,
                                related_name=_('order_item_product'))
    price = models.OneToOneField(Product, verbose_name=_('Price'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f'{self.product} - {self.order}'


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255, )
    iban = models.CharField(verbose_name=_('IBAN'), validators=[IBAN_REGEX], max_length=34, unique=True)
    bank_name = models.CharField(verbose_name=_('Bank Name'), max_length=255)
    order = models.ForeignKey(Order, verbose_name=_('Order'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('order bank account')
        verbose_name_plural = _("order bank accounts")

    def __str__(self):
        return f"{self.name} - {self.bank_name} - {self.order}"
