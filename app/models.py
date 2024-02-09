from django.db import models

# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)

    def __str__ (self):
        return self.sname

class Student(models.Model):
    stname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__ (self):
        return self.stname