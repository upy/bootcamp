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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from baskets.views import BasketViewSet
from core.views import APITokenObtainPairView
from customers.views import AddressViewSet, CityViewSet, \
    CountryViewSet, AdminCustomerViewSet, MyProfileViewSet, CustomerRegisterViewSet
from ecommerce.router import router
from orders.views import OrderViewSet
from payments.views import BankAccountViewSet, BankViewSet
from products.views import ProductViewSet, CategoryViewSet, AdminProductViewSet, \
    PriceViewSet

router.register("products", ProductViewSet)
router.register("prices", PriceViewSet)
router.register("categories", CategoryViewSet)
router.register("baskets", BasketViewSet)
router.register("addresses", AddressViewSet)
router.register("cities", CityViewSet)
router.register("countries", CountryViewSet)
router.register("orders", OrderViewSet)
router.register("bank_accounts", BankAccountViewSet)
router.register("banks", BankViewSet)
router.register("admin-products", AdminProductViewSet, basename="admin-product")
router.register("admin-customers", AdminCustomerViewSet, basename="admin-customer")
router.register("register", CustomerRegisterViewSet, basename="customer-register")


urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', APITokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile/', MyProfileViewSet.as_view(
        {"get": "retrieve", "put": "update", "patch": "partial_update"}), name='profile'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]
