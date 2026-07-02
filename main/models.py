from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.CharField(primary_key=True,max_length=90)
    password = models.CharField(null=True,blank=True)
    video = models.CharField(null=True,blank=True)

class AnimeDB(models.Model):
    name = models.CharField(primary_key=True)
    link = models.CharField(null=True)