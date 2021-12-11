"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from baskets.views import BasketItemViewSet, BasketViewSet
from customers.views import CustomerViewSet, AddressViewSet, CityViewSet, CountryViewSet
from ecommerce.router import router
from orders.views import OrderItemViewSet, OrderViewSet, BillingAddressViewSet, ShippingAddressViewSet, \
    OrderBankAccountViewSet
from products.views import ProductViewSet, CategoryViewSet

router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("basket_items", BasketItemViewSet)
router.register("baskets", BasketViewSet)
router.register("customers", CustomerViewSet)
router.register("addresses", AddressViewSet)
router.register("cities", CityViewSet)
router.register("countries", CountryViewSet)
router.register("order_items", OrderItemViewSet)
router.register("orders", OrderViewSet)
router.register("billing_address", BillingAddressViewSet)
router.register("shipping_address", ShippingAddressViewSet)
router.register("order_bank_account", OrderBankAccountViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
