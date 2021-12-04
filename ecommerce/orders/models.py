from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from core.validate_regex import validatePhoneNumber, validatePostCode, validateIBANNumber
from baskets.models import Basket
from customers.models import City, Customer
from products.models import Product, Price


class BillingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255,
                                verbose_name=_("Fullname"))
    line1 = models.CharField(max_length=200,
                             verbose_name=_("Line 1"))
    line2 = models.CharField(max_length=200,
                             verbose_name=_("Line 2"))
    phone = models.CharField(max_length=50,
                             verbose_name=_("Phone Number"),
                             validators=[validatePhoneNumber()]
                             )
    post_code = models.CharField(max_length=50,
                                verbose_name=_("Postcode"),
                                validators=[validatePostCode()]
                                )
    district = models.CharField(max_length=100,
                                 verbose_name=_("District"))
    city = models.ForeignKey(City,
                             verbose_name=_("City"),
                             on_delete=models.PROTECT)


    class Meta:
        verbose_name = _("Billing Address")
        verbose_name_plural = _("Billing Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.phone} - {self.district} - {self.city}"


class ShippingAddress(BaseAbstractModel):
    full_name = models.CharField(max_length=255,
                                verbose_name=_("Fullname"))
    line1 = models.CharField(max_length=200,
                             verbose_name=_("Line 1"))
    line2 = models.CharField(max_length=200,
                             verbose_name=_("Line 2"))
    phone = models.CharField(max_length=50,
                             verbose_name=_("Phone Number"),
                             validators=[validatePhoneNumber()]
                             )
    post_code = models.CharField(max_length=50,
                                verbose_name=_("Postcode"),
                                validators=[validatePostCode()]
                                )
    district = models.CharField(max_length=100,
                                 verbose_name=_("District"))
    city = models.ForeignKey(City,
                             verbose_name=_("City"),
                             on_delete=models.PROTECT)


    class Meta:
        verbose_name = _("Shipping Address")
        verbose_name_plural = _("Shipping Addresses")

    def __str__(self):
        return f"{self.full_name} - {self.phone} - {self.district} - {self.city}"


class OrderBankAccount(BaseAbstractModel):
    name = models.CharField(max_length=255,
                            verbose_name=_("Name"))

    iban = models.CharField(max_length=50,
                            verbose_name=_("IBAN"),
                            validators=[validateIBANNumber()],)
    bank_name = models.CharField(max_length=255,
                                 verbose_name=_("Bank Name"))

    class Meta:
        verbose_name = _("Order Bank Account")
        verbose_name_plural = _("Order Bank Accounts")

    def __str__(self):
        return f"{self.name} -  {self.bankName} - {self.iban}"


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer,
                                 verbose_name=_("Customer"),
                                 on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket,
                               verbose_name=_("Basket"),
                               on_delete=models.PROTECT)
    billing_address = models.ForeignKey(BillingAddress,
                                        verbose_name=_("Billing Address"),
                                        on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(ShippingAddress,
                                         verbose_name=_("Shipping Address"),
                                         on_delete=models.PROTECT)
    total_price = models.DecimalField(verbose_name=_("Total Price"),
                                      max_digits=15,
                                      decimal_places=2)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.customer} - {self.basket} - {self.total_price}"


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE)
    product = models.CharField(max_length=50,
                               verbose_name=_("Product"),
                               )
    price = models.DecimalField(verbose_name=_("Price"),
                                max_digits=10,
                                decimal_places=2)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Orders Items")

    def __str__(self):
        return f"{self.order} - {self.product} - {self.price}"