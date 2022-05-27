from django.db import models
from django import forms
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


    def __str__(self):
        return self.username

'''class LoginModel(models.Model):
    
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username'''

'''class SignupModel(models.Model):
    
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username'''