from django.shortcuts import render,get_object_or_404
from Home.models import Project
from Home.models import Post
import requests

# Create your views here.
def index(request):
    projects = Project.objects.all()
    posts = Post.objects.all()

    github_user = {}
    github_repos = []

    try:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10",
        }

        # GitHub profile
        user_response = requests.get(
            "https://api.github.com/users/kathan1999",
            headers=headers,
            timeout=5,
        )

        if user_response.ok:
            github_user = user_response.json()

        # Latest repositories
        repos_response = requests.get(
            "https://api.github.com/users/kathan1999/repos",
            params={
                "sort": "updated",
                "direction": "desc",
                "per_page": 6,
                "type": "owner",
            },
            headers=headers,
            timeout=5,
        )

        if repos_response.ok:
            github_repos = repos_response.json()

    except requests.RequestException:
        # Portfolio should still work if GitHub is temporarily unavailable.
        github_user = {}
        github_repos = []

    return render(request, "portfolio.html", {
        "projects": projects,
        "posts": posts,
        "github_user": github_user,
        "github_repos": github_repos,
    })

def blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog.html', {'post':post})