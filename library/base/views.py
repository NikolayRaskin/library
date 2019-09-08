from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.models import User_Profile, Book
from .regForm import RegForm

from rest_framework import viewsets
from base.serializers import User_ProfileSerializer, BookSerializer

import re
import datetime


class User_ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            try:
                new_reg_user = new_user(form)
                new_reg_user.save()
                login(request,new_reg_user.user)
                return redirect('/')
            except IntegrityError:
                messages.info(request, 'Login already exists!')
            except EmailExists:
                messages.info(request, 'Email already exists!')
            except PassAndConfirmDontMatch:
                messages.info(request, 'Pass and confirm pass don\'t match!')
        else:
            messages.info(request, 'Invalid form!')
    else:
        form = RegForm()
    return render(request,'registration/registration.html',{'form':form})

@login_required
def index(request):
    try:
        users = User_Profile.objects.all()
    except User_Profile.DoesNotExist:
        return Http404('User doesn\'t exist!')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            try:
                new_user(form).save()
            except IntegrityError:
                messages.info(request, 'Login already exists!')
            except EmailExists:
                messages.info(request, 'Email already exists!')
            except PassAndConfirmDontMatch:
                messages.info(request, 'Pass and confirm pass don\'t match!')
            return redirect('/')
        else:
            messages.info(request, 'Invalid form!')
    else:
        form = RegForm()
    context = {
        'users':users,
        'form':form,
    }
    return render(request,'base/index.html',context)

def new_user(form):
    user_name = form.cleaned_data['user_name']
    user_email = form.cleaned_data['user_email']
    user_firstname = form.cleaned_data['user_firstname']
    user_lastname = form.cleaned_data['user_lastname']
    birth_date = form.cleaned_data['birth_date']
    user_pass = form.cleaned_data['password']
    user_pass_confirm = form.cleaned_data['confirm_password']
    date_joined = datetime.datetime.now().date()
    
    new_user = User_Profile()
    if User.objects.filter(email=user_email).exists():
        raise EmailExists()
    if user_pass != user_pass_confirm:
        raise PassAndConfirmDontMatch()
    new_user.user = User.objects.create_user(user_name, user_email, user_pass)
    new_user.user_firstname = user_firstname
    new_user.user_lastname = user_lastname
    new_user.birth_date = birth_date

    return new_user
@login_required
def removeUser(request, id):
    user = User.objects.get(pk = id)
    user.delete()
    return redirect('index')

class EmailExists(Exception):
    pass

class PassAndConfirmDontMatch(Exception):
    pass