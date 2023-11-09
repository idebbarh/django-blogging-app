from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index-page"),
    path("blog/",views.blogs,name="blogs-page"),
    path("blog/<slug>",views.blog,name="blog-page"),
]
