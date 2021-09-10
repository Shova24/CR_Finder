from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
# Create your models here.


class messeges(models.Model):
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    msg = models.TextField()

    def __str__(self):
        return self.email
    def get_absolute_url(self):
        return reverse('home')