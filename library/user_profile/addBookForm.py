from django import forms
from base.models import Book

class addBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author','title')