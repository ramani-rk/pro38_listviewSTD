from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from app.models import *

class SchoolList (ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #queryset=School.objects.filter(id=1)
    #template_name='app/school_list.html'

class SchoolDetail (DetailView):
    model=School
    context_object_name='sclobject'

# context_object_name is used to store the objects in form of dict.


# CreateView comes as ESMFO(Empty School Model Function Object )
# In Create & Update its all performs automatically (Model Form Creation,Inported to Views,Created MFO (model function object),Send MFO to FE by using Context,POST method, Collect data, Validation,save & return HttpResponse)

class SchoolCreate(CreateView):
    model=School
    fields='__all__'


# UpdateView comes with Data SMFO(School Model Function Object )

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'