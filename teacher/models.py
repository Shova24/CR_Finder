from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

#5
class Teacher(models.Model):
    T_id = models.CharField(max_length=50,default=None)
    T_name = models.CharField(max_length=50,default=None)
    profile = models.URLField(max_length=500,default=None)

    def __str__(self):
        return self.T_name
    
    def get_absolute_url(self):
        return reverse('view_teacher')