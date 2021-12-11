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

from ecommerce.router import router
from products.views import ProductViewSet, CategoryViewSet, StockViewSet, PriceViewSet
from baskets.views import BasketViewSet, BasketItemViewSet
from customers.views import CityViewSet, CountryViewSet, CustomerViewSet, AddressViewSet
from orders.views import ShippingAddressViewSet, BillingAddressViewSet, OrderBankAccountViewSet, OrderViewSet, \
    OrderItemViewSet
from payments.views import BankViewSet, BankAccountViewSet

# Router Registrations for Each End Point
router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("stocks", StockViewSet)
router.register("prices", PriceViewSet)
router.register("baskets", BasketViewSet)
router.register("basket-items", BasketItemViewSet)
router.register("cities", CityViewSet)
router.register("countries", CountryViewSet)
router.register("customers", CustomerViewSet)
router.register("addresses", AddressViewSet)
router.register("shipping-addresses", ShippingAddressViewSet)
router.register("billing-addresses", BillingAddressViewSet)
router.register("order-bank-accounts", OrderBankAccountViewSet)
router.register("orders", OrderViewSet)
router.register("order-items", OrderItemViewSet)
router.register("banks", BankViewSet)
router.register("bank-accounts", BankAccountViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
