from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from products import enums


class Product(BaseAbstractModel):
    sku = models.CharField(verbose_name=_("SKU"), max_length=100, unique=True)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(max_length=2000, verbose_name=_("Description"))
    color = models.CharField(
        choices=enums.Colors.choices, verbose_name=_("Color"), max_length=20)
    size = models.CharField(max_length=30, verbose_name=_("Size"))

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def categoryList(self):
        return "\n".join([p.name for p in self.category_set.all()])

    def __str__(self):
        return f"{self.sku} - {self.name}"


class Stock(BaseAbstractModel):
    product = models.OneToOneField(Product, verbose_name=_("Product"),
                                   on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))

    class Meta:
        verbose_name = _("stock")
        verbose_name_plural = _("stocks")

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class Price(BaseAbstractModel):
    product = models.OneToOneField(Product, verbose_name=_("Product"),
                                   on_delete=models.PROTECT)
    amount = models.DecimalField(verbose_name=_("Amount"),
                                 max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("price")
        verbose_name_plural = _("prices")

    def __str__(self):
        return f"{self.product} - {self.amount}"


class Category(BaseAbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    products = models.ManyToManyField(
        to='Product',
        through='Categorization',
        through_fields=('category', 'product'),
        verbose_name=_('Products')
    )

    def productList(self):
        return "\n".join([p.name for p in self.products.all()])

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return f"{self.name}"


class Categorization(BaseAbstractModel):
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        verbose_name=_("Category")
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        verbose_name=_("Product")
    )

    class Meta:
        verbose_name = _("categorization")
        verbose_name_plural = _("categorizations")

    def __str__(self):
        return f"{self.product} - {self.category}"
