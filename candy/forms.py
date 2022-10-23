from dataclasses import fields
from django import forms
from django.forms import ModelForm
from candy.models import CustomUser
from django.contrib.auth.hashers import make_password


class CustomUserForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    widget={
            'password':forms.PasswordInput(),
            }
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name','password','passport','preferred_location')

    def clean_password(self):
        password=self.cleaned_data.get('password', None)
        if self.instance.pk is not None:
            if not password:
                return self.instance.password
                
        return make_password(password)



        
