from django.shortcuts import render
from django.http import HttpResponse
from siteapp import models
from siteapp.models import Skill, Project, WorkExperience


# Create your views here.

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    work_experiences = WorkExperience.objects.all()
    return render(request, 'home/index.html',{
        'skills':skills,'projects':projects,'work_experiences':work_experiences
    })


