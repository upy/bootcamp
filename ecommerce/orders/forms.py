from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from orders.models import Order


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "shipping_address", "billing_address", "total_price")

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("total_price") and cleaned_data.get("total_price") < 10:
            raise ValidationError(message={"total_price": _("Total must be greater than 10")})
        return cleaned_data
