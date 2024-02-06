from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from .models import Departments,Doctors
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

@login_required(login_url='login')
def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    print(dict_docs)
    return render(request,'doctors.html',dict_docs)
def contact(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def department(request):
    dic_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dic_dept)

def registration(request):
    if request.method =="POST":
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['pwd']
        cpwd=request.POST['cpwd']
        if pwd==cpwd:
            myuser=User.objects.create_user(username,email,pwd)
            myuser.save()
            return redirect('login')
        else:
            return render(request,'registration.html',{'msg':'password not matching'})
    return render(request,'registration.html')
def loginn(request):
    if request.method =="POST":
        username=request.POST['username']
        print(username)
        pwd=request.POST['pwd']
        user=authenticate(request,username=username,password=pwd)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
            # return render(request,'home.html') 
        else:
            return redirect('registration')
    return render(request,'login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('home')

    
