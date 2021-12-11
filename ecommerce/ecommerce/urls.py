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

from baskets.views import BasketViewSet, BasketItemViewSet
from ecommerce.router import router
from payments.views import BankViewSet, BankAccountViewSet
from products.views import ProductViewSet, CategoryViewSet
from customers.views import *
from orders.views import *

router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("baskets", BasketViewSet)
router.register("basket-items", BasketItemViewSet)
router.register("customers", CustomerViewSet)
router.register("countries", CountryViewSet)
router.register("cities", CityViewSet)
router.register("addresses", AddressViewSet)
router.register("orders", OrderViewSet)
router.register("order-items", OrderItemViewSet)
router.register("billing-addresses", BillingAddressViewSet)
router.register("shipping-addresses", ShippingAddressViewSet)
router.register("order-bank-accounts", OrderBankAccountViewSet)
router.register("banks", BankViewSet)
router.register("bank-accounts", BankAccountViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
