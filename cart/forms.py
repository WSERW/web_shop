from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='Количество', widget=forms.TextInput(attrs={'id':'quantityInp','value':1,'pattern':'[0-9]*'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)