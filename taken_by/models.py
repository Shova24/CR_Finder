from django.db import models
from batch.models import *
from course.models import *
from CR.models import *
from semester.models import *
from teacher.models import *



# Create your models here.
class Course_taken(models.Model):
    semester = models.ForeignKey(Semester, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Section_add, null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.course)

    def get_absolute_url(self):
        return reverse('view')
