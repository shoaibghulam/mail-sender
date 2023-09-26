from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, default="")
    email=models.CharField(max_length=100)
    university=models.CharField(max_length=150, default="")


    def __str__(self):
        return self.name



class myFiles(models.Model):
    mid=models.AutoField(primary_key=True)
    cv= models.FileField(upload_to='uploads/')
    project= models.FileField(upload_to='uploads/')
