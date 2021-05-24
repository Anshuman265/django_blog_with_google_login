from django.shortcuts import render, redirect
from django.contrib import messages
# dot here means the current directory
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        #Form created when the method is POST , i.e when the user is sending the data
        form =UserRegisterForm (request.POST)
        if form.is_valid():
            #Saving the form
            form.save()
            #Obtaining the username input of the form
            username  = form.cleaned_data.get('username')
            #Displaying flash messages on successful creation of the account
            messages.success(request, f'Account creation successful! Login with {username}')
            #Redirecting the user to the Login Page after creating account
            return redirect('login')
    else:
        form = UserRegisterForm ()
    return render(request, 'users/register.html' , {'form':form})
#Adding a decorator below to make login mandatory for the user to view profile
@login_required
def profile(request): 
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user) #Adding the arguments to pre fill the data in the form 
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile) #Adding the arguments to pre fill the data in the form 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile has been Updated!')
            return redirect('profile')
    else:
         u_form = UserUpdateForm(instance = request.user) #Adding the arguments to pre fill the data in the form 
         p_form = ProfileUpdateForm(instance = request.user.profile) #Adding the arguments to pre fill the data in the form 
    #Making a context dictionary to pass on to our template
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)