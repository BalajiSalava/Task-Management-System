from django.db import models


# Create your models here.
class Task(models.Model):
    Title=models.CharField(max_length=50)
    Disc=models.CharField(max_length=500)
    Created=models.DateField(auto_now=True)
    


class Restore(models.Model):
    Title=models.CharField(max_length=50)
    Disc=models.CharField(max_length=500)
    Created=models.DateField(auto_now=True)
   

class About(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField(max_length=10)
    email=models.EmailField()
    suggestions=models.TextField()
