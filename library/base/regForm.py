from django import forms
import datetime
from django.core.exceptions import ValidationError
class RegForm(forms.Form):
    user_name = forms.CharField(label='Login:', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Login'}))    
    user_email = forms.EmailField(label='Email:',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    user_firstname = forms.CharField(label='First name:', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'First name'})) 
    user_lastname = forms.CharField(label='Last name:', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Last name'}))    
    birth_date = forms.DateField(
        label='Birth date (d/m/yyyy) format',
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',)
        )
    password = forms.CharField(label='Password:',widget=forms.PasswordInput())    
    confirm_password = forms.CharField(label='Confirm password:',widget=forms.PasswordInput())

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        if birth_date >= datetime.date.today():
            raise ValidationError('Invalid birth date!')

        return birth_date