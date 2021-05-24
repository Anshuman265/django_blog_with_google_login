# Create your models here.
from django.db import models
#Importing our user here
from django.contrib.auth.models import User
#Importing pillow 
from PIL import Image 

class Profile(models.Model):
    #Making a one to one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile picture
    image = models.ImageField(default='default.jpg' , upload_to = 'profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #Creating a Image Variable
        img = Image.open(self.image.path)
        #Now checking the dimensions of the image
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)