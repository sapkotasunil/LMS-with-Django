from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class RoleOptions(models.TextChoices):
        ADMIN='admin','Admin' #admin(left side) used for store and Admin (Right Side)used for display
        EMPLOYER='employer',"Employer"
        EMLOYEE= "employee","Employee"
    
    class GenderOption(models.TextChoices):
        MALE='male','Male'
        FEMALE='female',"Female"
        OTHER='other','other'
        
        
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.CharField(blank=True,null=True)#dob should be null 
    adress=models.CharField(blank=True,null=True, max_length=100)
    phone=models.CharField(blank=True, null=True ,max_length=10)
    role=models.CharField(choices=RoleOptions,default=RoleOptions.EMLOYEE,max_length=10)
    gender=models.CharField(choices=GenderOption, default=GenderOption.MALE,max_length=8,null=True)
    image= models.FileField( upload_to="userImage",null=True)