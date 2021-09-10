from django import forms
from django.db.models import fields
from .models import *

class courseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('code', 'title')
        
        widgets = {
            'code' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'this is ID'}),
            'title' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'this is name'}),
        }

