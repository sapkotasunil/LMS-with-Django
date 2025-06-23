from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    class StatusOption(models.TextChoices):
        PENDING="Pending","Pending"
        IN_PROGRESS= "In_progress","In_progress"
        COMPLETED="Completed","completed"
        CANCELED= "Canceled","canceled"
        
    title=models.CharField(max_length=25)
    description=models.TextField( max_length=50 ,blank=True )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateField( editable=False, auto_now_add=True)
    status=models.CharField(choices=StatusOption,default=StatusOption.PENDING)
    update_at=models.DateField( auto_now=True, null=True, blank=True,editable=False)
    
