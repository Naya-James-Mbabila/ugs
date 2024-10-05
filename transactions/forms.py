from django import forms
from django.forms import formset_factory
from decimal import Decimal
from .models import (
    
    SaleBill, 
    SaleItem,
    SaleBillDetails
)
from inventory.models import Stock


# form used to get customer details
class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '^[\w\s\.,\-\/]+$', 'title' : 'Alphanumeric, spaces, and some symbols allowed', 'required': 'true'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['mode_of_payment'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['sales_agent'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = SaleBill
        fields = ['name', 'phone', 'mode_of_payment', 'sales_agent']

# form used to render a single stock item form
class SaleItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['perprice'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
    class Meta:
        model = SaleItem
        fields = ['stock', 'quantity', 'perprice']

# formset used to render multiple 'SaleItemForm'
SaleItemFormset = formset_factory(SaleItemForm, extra=1)

# form used to accept the other details for sales bill
class SaleDetailsForm(forms.ModelForm):
    class Meta:
        model = SaleBillDetails
        fields = ['total']
        
