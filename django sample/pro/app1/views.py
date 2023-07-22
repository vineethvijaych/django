from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models  import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.user.is_authenticated:
        d={
        'stud': student.objects.all()
           }
        return render(request,'home.html',d)
    else:
        return render (loginpage)

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

def edit(request,s_id):
    ed=student.objects.get(id=s_id)
    if request.method=='POST':
        e_id=request.POST.get('number')
        f_name=request.POST.get('fname')
        l_name=request.POST.get('lname')
        course=request.POST.get('cname')
        student.objects.filter(id=s_id).update(student_id=e_id,student_name=f_name,lname=l_name,course_name=course)
        return redirect(table)
    return render(request,'edit.html',{'ed':ed})


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def reg(request):
    if request.user.is_authenticated:
        return render (request,'home.html')
    else:
        if request.method=="POST":
            username=request.POST.get('uname')
            email=request.POST.get('useremail')
            password=request.POST.get('pswd')
            cpass=request.POST.get('cswd')

            if password==cpass:
                if User.objects.filter(username=username,email=email).exists():
                    print("username is exist")
                else:
                    new_user=User.objects.create_user(username,email,password)
                    new_user.save()
                    print("user created")
                    return redirect(loginpage)
            else:
                print("wrong password")
    return render (request,'login.html')


def loginpage(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        if request.method=="POST":
            username= request.POST.get('username')
            password= request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(home)
            else:
                print('user not exists')
                return redirect(reg)
    return render(request,'reg.html')


@login_required
def userlogout(request):
    logout(request)
    return redirect(loginpage)

