from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    DOB=models.DateField()
    email=models.EmailField()
    re_enter=models.EmailField()

