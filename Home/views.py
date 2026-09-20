from django.shortcuts import render,get_object_or_404
from Home.models import Project
from Home.models import Post

# Create your views here.
def index(request):
    projects = Project.objects.all()
    posts = Post.objects.all()
    return render(request, 'portfolio.html', {
        'projects':projects,
        'posts':posts
    })

def blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog.html', {'post':post})