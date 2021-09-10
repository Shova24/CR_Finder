from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

# Create your models here.
class Batch(models.Model):
    name = models.CharField(max_length=30,primary_key= True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('add_batch')
    

class Section_add(models.Model):
    SECTION = (
			('A', 'A'),
			('B', 'B'),
            ('C', 'C'),
            ('D','D'),
            ('E','E'),
            ('F','F'),
            ('G','G'),
            ('H','H')
			) 
    section = models.CharField(max_length=10, null = True,choices=SECTION)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s %s" % (self.batch, self.section)

    class Meta:
        ordering = ['batch']

    def get_absolute_url(self):
        return reverse('add_sec')
















class Section(models.Model):
    sec = models.CharField(max_length=100,primary_key= True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s %s" % (self.batch, self.sec)

    class Meta:
        ordering = ['batch']
