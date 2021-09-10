from django.db import models
from batch.models import *

class CRR(models.Model):
    photo = models.ImageField(upload_to ='image_folder')
    name = models.CharField(max_length=200, null=True)
    section = models.ForeignKey(Section_add, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    facebook = models.URLField(max_length=500,default=None)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('add_cr')




# Create your models here.
class CR(models.Model):
    photo = models.ImageField(upload_to ='image_folder')
    name = models.CharField(max_length=200, null=True)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    facebook = models.URLField(max_length=500,default=None)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('add_cr')



