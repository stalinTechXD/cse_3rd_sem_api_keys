from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64)
    math = models.IntegerField()
    ddt = models.IntegerField()
    dat=models.IntegerField()
    ca=models.IntegerField()
    dm = models.IntegerField()
    op=models.IntegerField()
    dd=models.IntegerField()
    da=models.IntegerField()
    es=models.IntegerField()

