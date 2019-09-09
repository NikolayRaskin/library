from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.models import User_Profile
from user_profile.models import Book
from .addBookForm import addBookForm

from rest_framework import viewsets
from base.serializers import User_ProfileSerializer, BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@login_required
def user_profile(request, id):
    thisUser = User_Profile.objects.get(pk = id)
    books = Book.objects.filter(owner = thisUser)
    if request.method == 'POST':
        form = addBookForm(request.POST)
        if form.is_valid():
            new_book(form,thisUser).save()
            return redirect('user_profile', thisUser.id)
        else:
            messages.info(request, 'Invalid form!')
    else:
        form = addBookForm()
    context = {
        'thisUser':thisUser,
        'books':books,
        'form':form
    }
    return render(request,'user_profile/user_profile.html',context)

def new_book(form,thisUser):
    author = form.cleaned_data['author']
    title = form.cleaned_data['title']
    new_book = Book()
    new_book.owner = thisUser
    new_book.author = author
    new_book.title = title
    return new_book

@login_required
def editBook(request,id):
    book = Book.objects.get(pk=id)
    thisUser = User_Profile.objects.get(id = book.owner.id)
    form = addBookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('user_profile', thisUser.id)
    else:
        print('Form isn\'t valid!')
    context = {
        'form':form,
        'id':id,
    }
    return render(request,'user_profile/editBookForm.html',context)

@login_required
def removeBook(request,id):
    book = Book.objects.get(pk = id)
    userId = book.owner.id
    book.delete()
    return redirect('user_profile', userId)