from django import forms
from .models import Product

class SellForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "productID",
            "name",
            "price",
            "condition",
            "brand",
            "descriptionText",
            "available",
            "tags"
        )