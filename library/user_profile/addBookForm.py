from django import forms
from user_profile.models import Book

class addBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author','title')