from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _
from orders.models import Order, OrderItem


class OrderFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "total_price" )


class OrderItemFilter(filters.FilterSet):

    product = filters.CharFilter(label=_("Product Name"), lookup_expr="icontains" )

    class Meta:
        model = OrderItem
        fields = ("order", "product", "price")
