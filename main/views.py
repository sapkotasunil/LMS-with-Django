from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login



def index(request):
    return render(request,"pages/index.html")

def loginPage(request):
    return render(request,"pages/auth/login.html")

def registerPage(request):
    return render(request,"pages/auth/register.html")

def registerUser(request):
    if request.method=='POST':
        errors={}
        username=request.POST.get('userName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        if User.objects.filter(username=username).exists():
            return render(request,"pages/auth/register.html",{"errors":{"userName":"User with username already exists"}})
        
        if User.objects.filter(email=email).exists():
            return render(request,"pages/auth/register.html",{"errors":{"email":"Email Already exists"}})
        
        if password!=confirmPassword:
             return render(request,"pages/auth/register.html",{"errors":{"password":"Password doesnot match"}})
            
        if password==confirmPassword:
            user =User.objects.create_user(username,email,password)
            user.save()
            messages.success(request,"user created sucessfully")
            return redirect('/login')

def loginUser(request):
    if request.method=="POST":
        errors={}
        username=request.POST.get('userName')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user:
            authenticated_user=authenticate(request, username=username, password=password)
            if authenticated_user:
                login(request,authenticated_user)
                messages.success(request,"user logged sucessfully")
                return redirect("/")
            else:
                return render(request,"pages/auth/login.html",{"errors":{"password":"Invalid password"}})
        else:
            
            return render (request,"pages/auth/login.html",{"errors":{"userName":"invalid user"}})