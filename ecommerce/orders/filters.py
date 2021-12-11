from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from customers.filters import CityFilter


# class BillingAddressFilter(filters.Filter):
#     full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
#     phone = filters.CharFilter(label=_("Phone"))
#     city = CityFilter
#     class Meta:
#         model = BillingAddress
#         fields = ("full_name", "phone", "city")



