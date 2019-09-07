from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

import datetime

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_firstname = models.CharField(max_length=100, blank=True)
    user_lastname = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(_('Date of joined'), auto_now_add=True)
    
    def __str__(self):
        return self.user_firstname + ' ' + self.user_lastname
    
    def save(self, *args, **kwargs):
        today = datetime.date.today()
        if self.birth_date >= today:
            raise ValidationError('Birth Date isn\'t valid!')
        super().save(*args, **kwargs)  # Call the "real" save() method.

# Create your models here.
