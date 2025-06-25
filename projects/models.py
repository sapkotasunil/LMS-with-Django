from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    class StatusOption(models.TextChoices):
        PENDING="Pending","Pending"
        IN_PROGRESS= "In progress","In progress"
        COMPLETED="Completed","completed"
        CANCELED= "Canceled","canceled"
        
    title=models.CharField(max_length=25)
    description=models.TextField( max_length=50 ,blank=True )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField( editable=False, auto_now_add=True)
    status=models.CharField(choices=StatusOption,default=StatusOption.PENDING)
    update_at=models.DateTimeField( auto_now=True, null=True, blank=True,editable=False)
    
    def __str__(self):
        return self.title
