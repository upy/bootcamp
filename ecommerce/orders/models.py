from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from baskets.models import Basket
from core.models import BaseAbstractModel
from customers.models import Customer, City
from products.models import Product

phone_regex = RegexValidator(regex=r'^\+?1?\d{20}$',
                             message="Phone number must be entered in the format: '+999999999'. '+' sign and 19 digits")


class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(verbose_name=_("Full name"),
                                 max_length=100
                                 )
    line1 = models.CharField(verbose_name=_("Line 1"),
                             max_length=255
                             )
    line2 = models.CharField(verbose_name=_("Line 2"),
                             max_length=255
                             )
    phone = models.CharField(validators=[phone_regex],
                             max_length=20
                             )
    district = models.CharField(verbose_name=_("District"),
                                max_length=255
                                )
    postcode = models.CharField(verbose_name=_("Post code"),
                                max_length=20)

    # since we would like to keep city information,
    # we put PROTECT on_delete over city which could be deleted by mistake
    city = models.ForeignKey(City,
                             verbose_name=_("City"),
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("billing address")
        verbose_name_plural = _("billing addresses")

    def __str__(self):
        return f"{self.full_name} - {self.line1} - {self.line2} - {self.city}"


class InvoiceAddress(BaseAbstractModel):
    full_name = models.CharField(verbose_name=_("Full name"),
                                 max_length=100
                                 )
    line1 = models.CharField(verbose_name=_("Line 1"),
                             max_length=255
                             )
    line2 = models.CharField(verbose_name=_("Line 2"),
                             max_length=255
                             )
    phone = models.CharField(validators=[phone_regex],
                             max_length=20
                             )
    district = models.CharField(verbose_name=_("District"),
                                max_length=255
                                )
    postcode = models.CharField(verbose_name=_("Post code"),
                                max_length=20)

    # since we would like to keep city information,
    # we put PROTECT on_delete over city which could be deleted by mistake
    city = models.ForeignKey(City,
                             verbose_name=_("City"),
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("invoice address")
        verbose_name_plural = _("invoice addresses")

    def __str__(self):
        return f"{self.full_name} - {self.district} - {self.city}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer,
                                 verbose_name=_("Customer"),
                                 on_delete=models.CASCADE
                                 )

    basket = models.ForeignKey(Basket,
                               verbose_name=_("Basket"),
                               on_delete=models.CASCADE
                               )

    billing_address = models.ForeignKey(BillingAddress,
                                        verbose_name=_("Billing address"),
                                        on_delete=models.CASCADE
                                        )

    shipping_address = models.CharField(verbose_name=_("Shipping address"),
                                        max_length=255
                                        )

    total_price = models.DecimalField(verbose_name=_("Order total price"), max_digits=9, decimal_places=2, null=False)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket} - {self.total_price}"


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(verbose_name=_("Order bank account name"),
                            max_length=255
                            )

    iban = models.CharField(verbose_name=_("Account IBAN number"),
                            max_length=20
                            )
    bank = models.CharField(
                             verbose_name=_("Bank"),
                             max_length=255,
                             )
    order = models.ForeignKey(Order,
                              verbose_name=_("Order"),
                              on_delete=models.CASCADE
                              )

    class Meta:
        verbose_name = _("Order bank account")
        verbose_name_plural = _("Order bank accounts")

    def __str__(self):
        return f"{self.bank} - {self.iban} - {self.name}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order,
                              verbose_name=_("Order"),
                              on_delete=models.CASCADE
                              )
    product = models.ForeignKey(Product,
                                verbose_name=_("Product"),
                                on_delete=models.PROTECT
                                )
    price = models.DecimalField(verbose_name=_("Order item price"),
                                max_digits=9,
                                decimal_places=2
                                )

    class Meta:
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")

    def __str__(self):
        return f"{self.order} - {self.product} - {self.price}"
