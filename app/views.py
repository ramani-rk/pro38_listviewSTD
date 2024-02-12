from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView,DetailView
from app.models import *

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #queryset=School.objects.filter(id=1)
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

# context_object_name is used to store the objects in form of dict.