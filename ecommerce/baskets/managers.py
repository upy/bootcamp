from django.db import models


class BasketItemQuerySet(models.QuerySet):

    def action_detailed_list(self):
        return self.select_related("basket", "product") \
            .order_by('id')

    def action_detailed(self):
        return self.select_related("basket", "product") \
            .order_by('id')


class BasketQuerySet(models.QuerySet):

    def action_detailed_list(self):
        return self.select_related("customer",).order_by('id')

    def action_detailed(self):
        return self.select_related("customer", ).order_by('id')