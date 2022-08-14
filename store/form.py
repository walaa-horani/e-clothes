from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserProfileForm(ModelForm):
    class Meta:
        fields= ['name','phone','address','city','country']  
        

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', )        