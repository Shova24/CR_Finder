from django import forms
from django.db.models import fields
from .models import *

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ('name',)
        
        widgets = {
            'name' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'this is name'}),
        }

class SecForm(forms.ModelForm):
    class Meta:
        model = Section_add
        fields = ('batch', 'section')
        
        widgets = {
            'batch' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'Select batch'}),
            'section' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'Select Section'}),
        }

