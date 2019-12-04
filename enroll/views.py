from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import Data
from django.http import HttpResponse

def frontpage(request):
    return render(request,"frontpage.html")

def enrollment(request):
    user=request.POST['username']
    password=request.POST['password']
    if user=="Ansh" and password=="ansh@1234":
        return render(request,"secondpage.html")

    else:
        return render(request,"wrong.html")

def register(request):
    if request.method=='POST':
        data=Data()
        data.enrollmentNumber=request.POST['enrollmentNumber']
        data.name=request.POST['name']
        data.email=request.POST['email']
        data.Address=request.POST['Address']
        data.PhoneNumber=request.POST['PhoneNumber']
        data.Class=request.POST['Class']
        datas=Data.objects.all()
        for data1 in datas:
            if data1.enrollmentNumber==data.enrollmentNumber:
                return HttpResponse("<center><h1>Sorry the Enrollment Number already EXISTS!!!</h1></center>")
        data.save()
        return render(request,"secondpage.html")

    else:
        return render(request,"SignIn.html")

def details(request):
    if request.method=='POST':
        print("ansh")
        datas=Data.objects.all()
        for data1 in datas:
            if data1.enrollmentNumber==request.POST['enrollment']:
                return render(request,"detailsPage.html",{'data1':data1})
    return render(request,"secondpage.html")



def last(request):
    return render(request,"secondpage.html")
