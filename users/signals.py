from django.db.models.signals import post_save
#Here user is the sender
from django.contrib.auth.models import User
#Importing the reciever
from django.dispatch import receiver
#Importing the profile
from .models import Profile

@receiver(post_save,sender = User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
#**kwargs accepts any additional arguments here
@receiver(post_save,sender = User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()
        