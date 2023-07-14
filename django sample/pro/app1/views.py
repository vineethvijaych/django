from django.shortcuts import render,redirect
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

    if request.method =='POST':
        e_id=request.POST.get('number')
        f_name=request.POST.get('fname')
        l_name=request.POST.get('lname')
        course=request.POST.get('cname')
        ob = student(student_id=e_id,student_name=f_name,lname=l_name,course_name=course)
        ob.save()
        return redirect(table)
    
    return render(request,'form.html')

def delete(request,s_id):
    field=student.objects.get(id=s_id)
    field.delete()
    return redirect(table)