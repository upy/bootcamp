from core.models import BaseAbstractModel
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from products import enums


class Product(BaseAbstractModel):
    sku = models.CharField(verbose_name=_("SKU"), max_length=100, unique=True)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(max_length=2000, verbose_name=_("Description"))
    color = models.CharField(
        choices=enums.Colors.choices, verbose_name=_("Color"), max_length=20)
    size = models.CharField(max_length=30, verbose_name=_("Size"))
    categories = models.ManyToManyField(
        "products.Category",
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

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
    name = models.CharField(
        max_length=255,
        verbose_name=_("Category Name"),
        unique=True
    )
    slug = models.SlugField(
        unique=True,
        editable=False
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.slug:
            return super(Category, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.name)
            return super(Category, self).save(*args, **kwargs)
