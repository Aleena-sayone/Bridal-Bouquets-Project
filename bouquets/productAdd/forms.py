from django import forms
from .models import Product
from productAdd.choices import *

class ProductForm(forms.ModelForm):
    
    bouqet_type = forms.ChoiceField(label='Bouquets Type',widget=forms.Select, choices=BOUQUETS_CHOICES)
    
    flower_type = forms.ChoiceField(label='Flower Type',widget=forms.Select, choices=FLOWER_CHOICES)

    class Meta:
        model = Product
        fields = ['title','bouqet_type','price','flower_type','image']
        
# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)