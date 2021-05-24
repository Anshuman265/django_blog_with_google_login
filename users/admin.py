from django.contrib import admin
#Importing the profiles model 
from .models import Profile
# Register your models here
admin.site.register(Profile)