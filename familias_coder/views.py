from multiprocessing import context
from re import template
from django.shortcuts import render
from django.template import loader
from .models import Person
from django.http import HttpResponse

def person_list(request):
    template = loader.get_template('person_list.html')
    persons = Person.objects.all()
    print(persons)
    context = {
        'persons': persons,
        }
    return HttpResponse(template.render(context, request))
