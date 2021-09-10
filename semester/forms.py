from django import forms
from django.db.models import fields
from .models import *

class semForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('name', 'year')
        
        widgets = {
            'name' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'this is ID'}),
            'year' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'this is name'}),
        }

