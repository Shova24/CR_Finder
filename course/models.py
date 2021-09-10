from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

#5
class Course(models.Model):
    code = models.CharField(max_length=50,default=None)
    title = models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_course')