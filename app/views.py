from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy

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


# CreateView comes as ESMFO(Empty School Model Function Object ).Its used to Create the object.
# In Create & Update its all performs automatically (Model Form Creation,Inported to Views,Created MFO (model function object),Send MFO to FE by using Context,POST method, Collect data, Validation,save & return HttpResponse)

class SchoolCreate(CreateView):
    model=School
    fields='__all__'


# UpdateView comes with Data SMFO(School Model Function Object ). Its used to Update the existing object.

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


# DeleteView is Used For delete the Existing Data
# Reverse_lazy is used to after completing the action it will send to particular URL.
class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('SchoolList')
    