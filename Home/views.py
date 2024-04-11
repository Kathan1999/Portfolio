from django.shortcuts import render, HttpResponse
from Home.models import Introduction
from Home.models import Description
from Home.models import Skill
from Home.models import Contact
from Home.models import Project1
from Home.models import Project2
from Home.models import Project3

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, subject=subject, email=email, message=message)
        contact.save()
    allIntro = Introduction.objects.all()
    allDescription = Description.objects.all()
    allSkill = Skill.objects.all()
    allProject1 = Project1.objects.all()
    allProject2 = Project2.objects.all()
    allProject3 = Project3.objects.all()
    context = {'allIntro':allIntro, 'allDescription':allDescription, 'allSkill':allSkill, 'allProject1':allProject1, 'allProject2':allProject2, 'allProject3':allProject3}
    return render(request, 'index.html', context)