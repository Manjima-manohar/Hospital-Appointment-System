from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from .models import Departments,Doctors
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html',)
def about(request):
    return render(request,'about.html')
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
def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dic_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dic_dept)
def home(request):
    return render(request,'home.html')
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

def user_logout(request):
    logout(request)
    return redirect('index')

    
