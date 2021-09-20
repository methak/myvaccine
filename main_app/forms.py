from django.forms import ModelForm
from .models import Vaccine
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
   
class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1' ,'password2' )