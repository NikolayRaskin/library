from django.db import models
from base.models import User_Profile

class Book(models.Model):
    owner = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author + ': ' + self.title
