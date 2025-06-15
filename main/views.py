from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render(request,"pages/index.html")

def loginPage(request):
    return render(request,"pages/auth/login.html")

def registerPage(request):
    return render(request,"pages/auth/register.html")

def registerUser(request):
    if request.method=='POST':
        username=request.POST.get('userName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        if User.objects.filter(username=username).exists():
            #first way to send error in frontend
            return render(request,"pages/auth/register.html",{"error":"User with username already exists"})
        
        if User.objects.filter(email=email).exists():
            #second way to send error in frontend(better)
            messages.error(request,"Email Already exists")
            return render(request,"pages/auth/register.html")
        
        if password!=confirmPassword:
             messages.error(request,"Password doesnot match")
             return render(request,"pages/auth/register.html")
            
        if password==confirmPassword:
            user =User.objects.create_user(username,email,password)
            
            user.save()
            messages.success(request,"user created sucessfully")
            return redirect('/login')
