
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, null = False)
    program = models.CharField(max_length=100, null = True)

class Wing(models.Model):
    name = models.CharField(max_length=1000, null = False)



class member(models.Model):
    first_name = models.CharField(max_length=100, null = False)
    last_name = models.CharField(max_length=100, null=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.IntegerField(default=0)

