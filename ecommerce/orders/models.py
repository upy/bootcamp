from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseAbstractModel
from phonenumber_field.modelfields import PhoneNumberField
from customers.models import City, Customer, Address
from django_iban.fields import IBANField
from baskets.models import Basket
from products.models import Product, Price


class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full Name'))
    line_1 = models.CharField(max_length=255, verbose_name=_('First Address Line'))
    line_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Second Address Line'))
    phone = PhoneNumberField()
    district = models.CharField(max_length=255, verbose_name=_("District"))
    postcode = models.CharField(max_length=255, verbose_name=_('Post Code'))
    city = models.ForeignKey(City, verbose_name=_('City'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return self.full_name


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_('Customer'),
                                 on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, verbose_name=_('Basket'),
                               on_delete=models.PROTECT)
    billing_address = models.ForeignKey(BillingAddress, verbose_name=_('Billing Address'),
                                        on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(Address, verbose_name=_('Shipping Address'),
                                         on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Amount"),
                                      max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f'{self.basket}'


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    iban = IBANField()
    bank_name = models.CharField(max_length=255, verbose_name=_("Bank Name"))
    order = models.ForeignKey(Order, verbose_name=_('Order'),
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f'{self.name}'


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, verbose_name=_('Order'),
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('Product'),
                                on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_("Amount"),
                                      max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f'{self.order}'

# Create your models here.
