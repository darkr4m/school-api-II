from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    student_email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    personal_email = models.EmailField(max_length=254, blank=True, unique=True)
    locker_number = models.IntegerField(default=110, unique=True)
    locker_combination = models.CharField(default="12-12-12", max_length=255)
    good_student = models.BooleanField(default=True, blank=False)