from email import message
from user.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from tasks.models import Task
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
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        dob=request.POST.get("dob")
        image=request.FILES.get("image")
        
        phone=request.POST.get("phone")
        adress=request.POST.get("adress")
        gender=request.POST.get("gender")
        
        
        if User.objects.filter(username=username).exists():
            return render(request,"pages/auth/register.html",{"errors":{"userName":"User with username already exists"}})
        
        if User.objects.filter(email=email).exists():
            return render(request,"pages/auth/register.html",{"errors":{"email":"Email Already exists"}})
        
        if len(phone)!=10:
            return render(request,"pages/auth/register.html",{"errors":{"phone":"Enter 10 digit number only"}})
        
        if password!=confirmPassword:
             return render(request,"pages/auth/register.html",{"errors":{"password":"Password doesnot match"}})
            
        if password==confirmPassword:
            user =User.objects.create_user(username=username,email=email,password=password, first_name=first_name,last_name=last_name)
            user.save()
            profile=Profile(user=user,dob=dob,adress=adress,phone=phone, gender=gender, role="employee",image=image)
            profile.save()
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
               
                return redirect("/dashboard")
            else:
                return render(request,"pages/auth/login.html",{"errors":{"password":"Invalid password"}})
        else:
            
            return render (request,"pages/auth/login.html",{"errors":{"userName":"invalid user"}})
@login_required(login_url="/login")        
def dashboard(request):
    role=request.user.profile.role
    if role=="employee":
        return redirect("/employee/dashboard")
    elif role=="employer":
        return redirect("/employer/dashboard")
    else:
        return redirect("/login")

@login_required(login_url="/login")        
def employerDashboard(request):
    role=request.user.profile.role
    if role =="employer":
        pendingTasks=Task.objects.filter(status="Pending",user=request.user)
        completedTasks=Task.objects.filter(status="Completed",user=request.user)
        InprogressTasks=Task.objects.filter(status="In Progress",user=request.user)
        return render(request,'pages/employer/dashboard.html',{'pendingTasks':pendingTasks, "completedTasks":completedTasks, "inProgressTasks":InprogressTasks})
    else:
        return redirect('employee/dashboard')


@login_required(login_url="/login")        
def employeeDashboard(request):
    role=request.user.profile.role
    if role =="employee":
        return render(request,'pages/employee/dashboard.html')
    else:
            return redirect('/employer/dashboard')
