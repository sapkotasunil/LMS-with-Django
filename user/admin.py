from django.contrib import admin 
from .models import *

class ProfileAdmin (admin.ModelAdmin):
    list_display= ('name','user','adress',)
    
admin.site.register(Profile,ProfileAdmin)
