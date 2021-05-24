# Create your views here.
from django.shortcuts import render
from .models import Post
from django.views.generic import ( ListView,
                                  DetailView,
                                  CreateView ,
                                  UpdateView,
                                  DeleteView
                                  )
#Importing for LoginValidation
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#Making a home page
def home(request):
    passon = {
        'p':Post.objects.all()
    }
    return render(request,'blog/home.html',passon) #The third argument here is used for passing the data . We are passing a dictionary here
#Making a list View for the Posts
class PostListView(ListView):
    model = Post
    #PostListView is looking for this:-
    #<app>/ <model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'p'
    ordering = ['-date_posted']
#Making a detail view for the Posts
class PostDetailView(DetailView):
    model = Post
#Creating a create View for the Posts
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    #Fields of the Post
    fields = ['title', 'content']
    #Adding validation while creating a Post
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#Creating a Update Class View Here
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    #Fields of the Post
    fields = ['title', 'content']
    #Adding validation while creating a Post
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #Test function
    def test_func(self):
        post = self.get_object()
        #This checks whether the currently logged in user is the same as the author of the post
        if self.request.user == post.author:
            return True
        return False
#Creating the delte view
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    #Redirecting the user after deleting the post
    success_url = '/'
        #Test function
    def test_func(self):
        post = self.get_object()
        #This checks whether the currently logged in user is the same as the author of the post
        if self.request.user == post.author:
            return True
        return False
#The about page
def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})