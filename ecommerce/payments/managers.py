from django.db import models


class BankAccountQuerySet(models.QuerySet):
    def action_detailed_list(self):
        return self.select_related("bank", ).order_by('id')

    def action_detailed(self):
        return self.select_related("bank", ).order_by('id')
