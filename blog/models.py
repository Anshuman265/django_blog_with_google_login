from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#Importing reverse
from django.urls import reverse
# Create your models here.
#Models in Django are made as classes
class Post(models.Model): #here the post class inherits the Models class
    title = models.CharField(max_length=100)    
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) #adding the auto_now_add at the end wil set the date_posted to current date time only when the obejct is created
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
        