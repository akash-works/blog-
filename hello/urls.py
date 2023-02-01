from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="index.html"),
    path('about/', about,name="about.html"),
    path('contact/', contact,name="contact.html"),
    path('post/', samp_post,name="post.html"),
    path('aka/', aka,name="aka"),
    path('sum/', sum,name="sum"),
    path('a/', a,name="a"),
    
    
]