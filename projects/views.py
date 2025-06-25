from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from tasks.models import Task


@login_required(login_url="/login")
def projects(request):
    role=request.user.profile.role
    if role=="employer":
        return redirect('/employer/projects')
    elif role=="employee":
        return redirect ('/employee/projects')
    else:
        return redirect ('/dashboard')
    
@login_required(login_url="/login")
def employerProjects(request):
    role=request.user.profile.role
    projects=Project.objects.filter(user=request.user)
    
    if role=="employer":
        return render (request,"pages/employer/project/project_page.html",{"projects":projects})
    else:
        return redirect('/emplyee/projects')

@login_required(login_url="/login")
def employeeProjects(request):
    role=request.user.profile.role
    if role=="employee":
        return render(request,"pages/employee/project/project_page.html")
    else:
        redirect('/employer/projects')
@login_required(login_url="/login")      
def register_project_page(request):
    return render(request,"pages/employer/project/register_project.html")

def createProject(request):
    errors={}
    user=request.user
    title=request.POST.get("title")
    description=request.POST.get('description')
    status=request.POST.get('status')
    
    if user.profile.role=="employer":
        if len(title)<3:
            errors["title"]= "Title length should be more than 3 characters."
        if description != "" and len(description)<10:
            errors["description"]= "Description length should be more than 10 characters."
        if errors:
            return render(request,"pages/employer/project/register_project.html",{"errors":errors})
        
        project=  Project(title=title,description=description,status=status,user=user)
        project.save()
        messages.success(request,"Project created sucessfully")
        return redirect('/employer/projects')
 
@login_required(login_url="/login")            
def employerProjectDetails(request,id):
    project=Project.objects.get(id=id)
    tasks=Task.objects.filter(project=project)
    
    return render(request,"pages/employer/project/project_details.html",{"project":project,'tasks':tasks})   
         
         
@login_required(login_url="/login") 
def editProjectDetailsPage( request,id):
    project=get_object_or_404(Project,pk=id)
    if request.user.profile.role== 'employer':
        return render (request,"pages/employer/project/edit_project.html",{"project":project })
    else:
        return redirect('/employee/projects')


                      
@login_required(login_url="/login")                       
def employeeProjectDetails(request,id):
    project=Project.objects.get(id=id)
    return render(request,"pages/employee/project/project_details.html",{"project":project})            
            
@login_required(login_url="/login")
def editProjectDetails(request,id):
    errors={}
    project=get_object_or_404(Project, pk=id)
    if request.method=='POST':
        title=request.POST.get("title")
        description=request.POST.get('description')
        status=request.POST.get('status')
        if request.user.profile.role=="employer":
            if len(title)<3:
                errors["title"]= "Title length should be more than 3 characters."
            if description != "" and len(description)<10:
                errors["description"]= "Description length should be more than 10 characters."
            if errors:
                 return render(request,"pages/employer/project/register_project.html",{"errors":errors})
            project.title=title
            project.description=description
            project.status=status
            project.save()
            messages.success(request,"project update sucessfully")
            return redirect(f"/employer/project_details/{id}") 
@login_required(login_url="/login")       
def deleteProject(request,id):
    if request.user.profile.role=="employer":
        project=get_object_or_404(Project, pk=id)
        project.delete()
        messages.success(request,"project deleted sucessfully")
        return redirect('/employer/projects')
            