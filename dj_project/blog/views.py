from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        "author": "CoreyMS",
        "title": "Blog Post",
        "content": "First post content",
        "date_posted": "August 27, 2018"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2018"
    }
]

# Create your views here.
def home(request):
    return HttpResponse("<h1>Blog Home</h1>")

def about(request):
    return HttpResponse("<h1>Blog About</h1>")

def rendered_home(request):
    context = {"posts": Post.objects.all()}
    return render(request, 'blog/home.html', context)

def rendered_about(request):
    return render(request, "blog/about.html", {"title": "About"})