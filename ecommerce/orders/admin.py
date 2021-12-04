from django.contrib import admin
from orders.models import (BillingAddress, Order, OrderBankAccount,
                                     OrderItem, ShippingAddress)

# Register your models here.
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderBankAccount)
admin.site.register(OrderItem)
