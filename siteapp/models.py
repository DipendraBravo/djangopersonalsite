from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,blank=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    url = models.URLField(blank=True)

class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()