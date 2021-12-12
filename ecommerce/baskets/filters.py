from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from baskets import enums as basket_enums
from products import enums as product_enums
from baskets.models import Basket, BasketItem
from products.filters import ProductFilter


class BasketFilter(filters.FilterSet):
    """
     Filter for BasketViewSet
    """
    customer_email = filters.CharFilter(label=_("Customer Email"), field_name='customer__email', lookup_expr='icontains')
    customer_firstname = filters.CharFilter(label=_("Customer First Name"), field_name='customer__first_name', lookup_expr='icontains')
    customer_lastname = filters.CharFilter(label=_("Customer Last Name"), field_name='customer__last_name', lookup_expr='icontains')
    status = filters.ChoiceFilter(label=_("Basket Status") ,choices=basket_enums.BasketStatus.choices)

    class Meta:
        model = Basket
        fields = ("customer", "customer_firstname", "customer_lastname", "customer_email", "status", )


class BasketItemFilter(filters.FilterSet):
    """
    Filter for BasketItemViewSet
    """
    basket_customer_email = filters.CharFilter(label=_("Customer Email"), field_name='basket__customer__email', lookup_expr='icontains')
    basket_customer_firstname = filters.CharFilter(label=_("Customer First Name"), field_name='basket__customer__first_name', lookup_expr='icontains')
    basket_customer_lastname = filters.CharFilter(label=_("Customer Last Name"), field_name='basket__customer__last_name', lookup_expr='icontains')
    basket_status = filters.ChoiceFilter(label=_("Basket Status"), field_name='basket__status', choices=basket_enums.BasketStatus.choices)
    product_name = filters.CharFilter(label=_("Product Name"), field_name='product__name', lookup_expr='icontains')
    product_color = filters.ChoiceFilter(label=_("Product Color"), field_name='product__color', choices=product_enums.Colors.choices)
    product_size = filters.CharFilter(label=_("Product Size"), field_name='product__size', lookup_expr='exact')
    product_category = filters.CharFilter(label=_("Product Category"), field_name='product__categories__name', lookup_expr='icontains')
    price = filters.NumberFilter(label=_("Price"))
    product = ProductFilter
    basket = BasketFilter

    class Meta:
        model = BasketItem
        fields = ("basket", "basket_status", "product", "quantity", "price","basket_customer_email","basket_customer_firstname","basket_customer_lastname",)
