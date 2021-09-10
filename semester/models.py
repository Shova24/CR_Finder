from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

#5
class Semester(models.Model):
    Name = (
			('Spring', 'Spring'),
			('Summer', 'Summer'),
            ('Fall', 'Fall')
			) 
    name = models.CharField(max_length=10, null = True,choices=Name)
    year = models.CharField(max_length=50,default=None)
    def __str__(self):
        return "%s %s" % (self.name, self.year)
        
    
    def get_absolute_url(self):
        return reverse('add_sem')