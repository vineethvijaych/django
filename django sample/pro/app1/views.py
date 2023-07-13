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
    d={
        'stud': student.objects.all()
    }
    return render(request,'table.html',d)

def image(request):
    d={
        'fields':pictures.objects.all()
    }
    return render(request,'image.html',d)

def form(request):
    
    return render(request,'form.html')