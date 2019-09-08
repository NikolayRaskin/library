from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

import datetime

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

