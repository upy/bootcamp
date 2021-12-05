from django.db import models


class ProductQuerySet(models.QuerySet):
    def banner_products(self):
        return self.filter(stock__quantity__gte=10, price__amount__lt=100)

    def has_stock(self):
        return self.filter(stock__quantity__gt=0)
