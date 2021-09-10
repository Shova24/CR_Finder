from django import forms
from django.db.models import fields
from .models import *

class CR_Form(forms.ModelForm):
    class Meta:
        model = CRR
        fields = ('photo', 'name', 'section', 'phone', 'email', 'facebook')
        
        widgets = {

            'name' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'Enter CR\'s name'}),
            'section' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'Select Section'}),
            'phone' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'Enter Contact Number'}),
            'email' : forms.EmailInput(attrs= {'class' : 'form-control', 'placeholder': 'Select Section'}),
            'facebook' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'Enter Contact Number'}),
        }

