from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password1=models.CharField(max_length=8)
    password2=models.CharField(max_length=8)
    def __str__(self):
        return self.title