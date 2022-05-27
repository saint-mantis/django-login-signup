from django.shortcuts import render
from pathlib import Path
import os
from .models import User
from django.http import HttpResponseForbidden
from .forms import LoginForm,SignupForm

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    request.session["UserExists"] = []
    request.session["UserExistsarray"] = []
    def Authenticate(username,password):
        #user = auth.authenticate(username=username, password=password)
        a=User.objects.filter(username=username,password=password).exists()
        print(f'the a is {a}')
        if a == True:
            request.session["UserExistsarray"].append("True")
        elif a == False:
            request.session["UserExistsarray"].append("False")

        print(f'UserExistsarray is {request.session["UserExistsarray"]}')
        if request.session["UserExistsarray"][0] == "False":
            UserExists="Usernot found"
            print(UserExists)
            request.session["UserExists"].append("False")
            Userstatus=print(request.session["UserExists"][0])
            
        elif request.session["UserExistsarray"][0] == "True":
            UserExists="User exists"
            print(UserExists)
            request.session["UserExists"].append("True")
            Userstatus=print(request.session["UserExists"][0])

            
            
     
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        UserExists=Authenticate(username,password)
        Userstatus=request.session["UserExists"]
        print(Userstatus)
        if Userstatus[0]=="True":
            return render(request, 'index.html', {'UserExists':UserExists,'username':username})
        else:
            Usernotfound= "User not found"
            form=LoginForm()
            return render(request, 'authentication-login1.html', {'UserExists':Usernotfound,'form':form})
    form=LoginForm()
    context={'form':form,}
    return render(request, 'authentication-login1.html',context)


def signup(request):
    request.session["SignupUser"] = []
    form = SignupForm()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        model = User.objects.create(username=username,password=password,email=email)
        model.save()
        return render(request, 'index.html', {'username':username})
    return render(request, 'authentication-register1.html', {'form':form})