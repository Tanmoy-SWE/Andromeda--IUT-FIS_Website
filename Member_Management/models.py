
from django.db import models


# Create your models here.

class member(models.Model):
    first_name = models.CharField(max_length=100, null = False)
    last_name = models.CharField(max_length=100, null=False)
    dept = models.CharField(max_length=100, null=False)
    program = models.CharField(max_length=100, null=False)
    student_id = models.IntegerField(default=0)

class members(models.Model):
    first_name = models.CharField(max_length=100, null = False)
    last_name = models.CharField(max_length=100, null=False)
    dept = models.CharField(max_length=100, null=False)
    program = models.CharField(max_length=100, null=False)
    student_id = models.IntegerField(default=0)
