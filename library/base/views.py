from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.models import User_Profile
from .regForm import RegForm

import re
import datetime

def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_firstname = form.cleaned_data['user_firstname']
            user_lastname = form.cleaned_data['user_lastname']
            birth_date = form.cleaned_data['birth_date']
            user_pass = form.cleaned_data['password']
            user_pass_confirm = form.cleaned_data['confirm_password']
            date_joined = datetime.datetime.now().date()
            
            new_user = User_Profile()
            new_user.user = User.objects.create_user(user_name, user_email, user_pass)
            new_user.user_firstname = user_firstname
            new_user.user_lastname = user_lastname
            new_user.birth_date = birth_date
            new_user.save()

            login(request,new_user.user)
            return redirect('/')
        else:
            print('======================Form isn\'t valid======================')
    else:
        form = RegForm()
    return render(request,'registration/registration.html',{'form':form})

@login_required
def index(request):
    try:
        users = User_Profile.objects.all()
    except User_Profile.DoesNotExist:
        return Http404('User doesn\'t exist!')
    context = {
        'users':users,
    }
    return render(request,'base/index.html',context)

def user_profile(request, id):
    thisUser = User_Profile.objects.get(pk = id)
    context = {
        'thisUser':thisUser,
    }
    return render(request,'base/user_profile.html',context)

def removeUser(request, id):
    user = User.objects.get(pk = id)
    user.delete()
    return redirect('index')
