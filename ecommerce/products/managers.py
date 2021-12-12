from django.db import models


class ProductQuerySet(models.QuerySet):
    def banner_products(self):
        return self.filter(stock__quantity__gte=10, price__amount__lt=100)

    def has_stock(self):
        return self.filter(stock__quantity__gt=0)

    def action_detailed_list(self):
        return self.prefetch_related("categories")

    def action_detailed(self):
        return self.prefetch_related("categories")