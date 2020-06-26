from django import forms
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = "__all__"

        widgets ={
            "prod_code": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Uniq Product Code e.g: AA982'}),
            "category": forms.Select(attrs={'class':'form-control'}),
            "unit_price": forms.TextInput(attrs={'class':'form-control'}),
            "image" : forms.FileInput(attrs={'class':'my-2'})
            }