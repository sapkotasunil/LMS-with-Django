from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages

def profilePage(request):
    return render(request,'pages/profile.html')

def logoutUSer(request):
    logout(request)
    messages.success(request,"you have sucesfully logout")
    return redirect("/")  
def editUser(request):
    return render(request,"pages/auth/edit_profile.html")

def update_edit(request):
    errors={}
    if request.method=="POST":
        user=request.user
        profile=user.profile
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        password= request.POST.get("password")
        confirm_password= request.POST.get("confirm_password")
        image= request.POST.get("image")
        phone= request.POST.get("phone")
        dob= request.POST.get("dob")
        gender= request.POST.get("gender")
        adress= request.POST.get("adress")
        
        if  confirm_password == password:
            errors["password"] = "Passwords do not match"
       
        if phone and len(phone) != 10:
             errors["phone"] = "Phone number must be 10 digits"
            
           
        if errors:
            return render(request,'pages/auth/edit_profile.html',{"errors":errors})
        
        user.first_name=first_name
        user.last_name=last_name
        profile.dob=dob
        profile.gender=gender
        profile.phone=phone
        if password:
            user.set_password(password)
            authenticated_user=authenticate(request,usernane=user.username,password=user.password)   
            login(request,authenticated_user)
            
        profile.image=image
        profile.adress=adress
        
        user.save()
        profile.save()
        messages.success(request,"profile update sucessfully")
        return redirect("/profile")
    

        
        
        
       
        