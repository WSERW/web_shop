from django import forms
from .models import Order, CallRequest

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'phone', 'address', 'city', 'delivery_way', 'comment']
class RequestCreateForm(forms.ModelForm):
    class Meta:
        model = CallRequest
        fields = ['name', 'phone']