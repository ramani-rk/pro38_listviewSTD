from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)


# get_absolute_url is used to done a dynamic URL mapping (or) canonical URL mapping and its a object method
# canonical URL mapping is a process of creating URL suffixes dynamically, based on selected instance.
# instance means currently presented address. self holds the address of the instance.

    def get_absolute_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})

# reverse is used to take the control flow to urls.py into respected url name

    def __str__ (self):
        return self.sname



class Student(models.Model):
    stname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__ (self):
        return self.stname