from django.shortcuts import render
from . models import *

# Create your views here.


def home(request):
    d = {
        'studs' : student.objects.all(),
        'deps': department.objects.all()
    }
    return render(request, 'home.html',d) 

def about(request):

    return render(request, 'about.html') 

