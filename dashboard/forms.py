from django import forms
from django.db.models import fields
from .models import *

class msgform(forms.ModelForm):
    class Meta:
        model = messeges
        fields = ('email', 'msg')

        widgets = {
            'email' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'Please enter your email'}),
            'msg' : forms.Textarea(attrs= {'class' : 'form-control'}),
        }