from django.db import models


class BasketQuerySet(models.QuerySet):
    def banner_products(self):
        """
        BasketItem can not be less then 10 and quantity greater or equal to 100
        """
        return self.filter(basketitem__quantity__gte=10, basketitem__quantity__lt=100)

    def basket_status(self):
        """
        Basket Status can not be submitted
        """
        return self.filter.exclude(basket__status="submitted")


