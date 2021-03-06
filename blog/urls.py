#Here routing of all webpages is written
from django.urls import path
from . import views #from dot - dot here means current directory 
#Importing the list view here
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
                    )
urlpatterns = [
    #path('',views.home, name='blog-home'),
    path('',PostListView.as_view(), name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]
#PostListView is looking for this:-
#<app>/ <model>_<viewtype>.html