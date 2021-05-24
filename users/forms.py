from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#User registration from inherits UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #Leaving this empty sets required=true by default
    class Meta: #Learn meta classes
        model = User #Model = user here says which field we want to work with
        fields = ['username', 'email' , 'password1' , 'password2'] #Specifying the fields which we will be using
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User #Specifying which model we want to work with
        fields = ['username','email'] #Specifying the fields which we want to work with
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        