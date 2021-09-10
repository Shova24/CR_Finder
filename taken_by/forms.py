from django import forms
from django.db.models import fields
from .models import *

class Take_Form(forms.ModelForm):
    class Meta:
        model = Course_taken
        fields = ('semester', 'course', 'section', 'teacher')
        
        widgets = {

            'semester' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'Select semester'}),
            'course' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'Select Section'}),
            'section' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'Select semester'}),
            'teacher' : forms.Select(attrs= {'class' : 'form-control', 'placeholder': 'Select Section'}),
           
        }

