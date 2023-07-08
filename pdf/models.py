from sys import maxsize
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    about = models.TextField(max_length=500)
    education = models.TextField(max_length=500)
    work_experience = models.TextField(max_length=500)
    interests = models.TextField(max_length=500)
    open_source_projects = models.TextField(max_length=500)

# Create your models here.
