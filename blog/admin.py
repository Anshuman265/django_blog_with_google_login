from django.contrib import admin
# Register your models here.
#Importing the Post model for registration here
from .models import Post
#After registering we can see the Post in the admin control Panel

admin.site.register(Post)
