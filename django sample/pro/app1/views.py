from django.shortcuts import render
from . models import *

def home(request):
    d={
        'stud': student.objects.all()
    }
    return render(request,'home.html',d)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def table(request):
    return render(request,'table.html')
