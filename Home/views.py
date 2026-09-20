from django.shortcuts import render, HttpResponse
from Home.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {
        'projects':projects
    })

def blog(request):
    return render(request, 'blog.html')