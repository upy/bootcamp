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

from customers.views import AddressViewSet, CityViewSet, CountryViewSet, CustomerViewSet
from ecommerce.router import router
from products.views import PriceViewSet, ProductViewSet, CategoryViewSet, StockViewSet
from payments.views import BankAccountViewSet, BankViewSet
from orders.views import BillingAddressViewSet, OrderBankAccountViewSet, \
    OrderItemViewSet, OrderViewSet, ShippingAddressViewSet
from baskets.views import BasketItemViewSet, BasketViewSet

router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("stocks", StockViewSet)
router.register("prices", PriceViewSet)
router.register("banks", BankViewSet)
router.register("bank-accounts", BankAccountViewSet)
router.register("billing-addresses", BillingAddressViewSet)
router.register("shipping-addresses", ShippingAddressViewSet)
router.register("orders", OrderViewSet)
router.register("order-bank-accounts", OrderBankAccountViewSet)
router.register("order-items", OrderItemViewSet)
router.register("cities", CityViewSet)
router.register("countries", CountryViewSet)
router.register("customers", CustomerViewSet)
router.register("addresses", AddressViewSet)
router.register("baskets", BasketViewSet)
router.register("basket-items", BasketItemViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
