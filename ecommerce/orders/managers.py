from django.db import models


class BillingAddressQuerySet(models.QuerySet):

    def action_detailed_list(self):
        return self.select_related("city", ).order_by('id')

    def action_detailed(self):
        return self.select_related("city", ).order_by('id')


class ShippingAddressQuerySet(models.QuerySet):

    def action_detailed_list(self):
        return self.select_related("city", ).order_by('id')

    def action_detailed(self):
        return self.select_related("city", ).order_by('id')


class OrderBankAccountQuerySet(models.QuerySet):

    def action_detailed_list(self):
        return self.select_related("order", ).order_by('id')

    def action_detailed(self):
        return self.select_related("order", ).order_by('id')


class OrderQuerySet(models.QuerySet):

    def action_detailed_list(self):
        return self.select_related("customer", "basket").order_by('id')

    def action_detailed(self):
        return self.select_related("customer", "basket").order_by('id')


class OrderItemQuerySet(models.QuerySet):

    def action_detailed_list(self):
        return self.select_related("order",).order_by('id')

    def action_detailed(self):
        return self.select_related("order",).order_by('id')
