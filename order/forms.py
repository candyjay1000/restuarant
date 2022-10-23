from django import forms
from django.forms import ModelForm
from order.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('order', 'quantity','email')