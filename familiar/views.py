from django.shortcuts import render
from django.http import HttpResponse
from .models import Person


def index(request):
    persons = Person.objects.all()
    contexto = {'personas': persons}
    return render(request,"familiar/index.html",contexto)



