from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import ugettext_lazy as _

from payments.models import Bank, BankAccount


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(label=_('Name'), method='filter_name')

    class Meta:
        model = Bank
        fields = ('name',)
    
    def filter_name(self, qs, name, value):
        return qs.filter(Q(name__icontains=value))


class BankAccountFilter(filters.FilterSet):
    # bank = filters.ModelChoiceFilter(
    #     field_name='bank', 
    #     queryset=Bank.objects.all(), 
    #     label=_('Bank'), 
    #     method="filter_name"
    # )

    name = filters.CharFilter(label=_('Name'), method='filter_name')

    class Meta:
        model = BankAccount
        fields = ('bank', 'name', 'iban')

    def filter_name(self, qs, name, value):
        return qs.filter(Q(name__icontains=value))