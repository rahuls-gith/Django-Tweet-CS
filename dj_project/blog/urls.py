from django.urls import path
from . import views

urlpatterns = [
    path("", views.rendered_home, name="blog-home"),
    path("about/", views.rendered_about, name="blog-about"),
    path("", views.home, name="bloghome"),
    path("about/", views.about, name="blog-about"),   
]