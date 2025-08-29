from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'unit', 'location', 'expiry_date', 'low_stock_threshold']
