# forms.py
from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=15, initial=1)
    item_id = forms.IntegerField(widget=forms.HiddenInput())
