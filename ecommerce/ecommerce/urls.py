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
from products.views import PriceViewSet, ProductViewSet, CategoryViewSet, StockViewSet
from payments.views import BankAccountViewSet, BankViewSet
from orders.views import BillingAddressViewSet, OrderBankAccountViewSet, \
    OrderItemViewSet, OrderViewSet, ShippingAddressViewSet

router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("stock", StockViewSet)
router.register("price", PriceViewSet)
router.register("bank", BankViewSet)
router.register("bank-account", BankAccountViewSet)
router.register("billing-address", BillingAddressViewSet)
router.register("shipping-address", ShippingAddressViewSet)
router.register("order", OrderViewSet)
router.register("order-bank-account", OrderBankAccountViewSet)
router.register("order-item", OrderItemViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
