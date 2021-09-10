from django import forms
from django.db.models import fields
from .models import *

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('T_id', 'T_name', 'profile')
        
        widgets = {
            'T_id' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'this is ID'}),
            'T_name' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'this is name'}),
            'profile' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'this is link'}),
        }

